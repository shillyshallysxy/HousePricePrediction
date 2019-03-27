from django.http import HttpResponse, JsonResponse
from .models import House, HistoryPrice, News, PredictPrice
from django.views.generic import View
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings
import pickle
from pymongo import MongoClient
from django_redis import get_redis_connection
import datetime
from dateutil.relativedelta import relativedelta
import json
import base64
from haystack.generic_views import SearchView
from drf_haystack.serializers import HaystackSerializer
import sys
import random
# url: house/price/<city>/history?last_n_month=xx
class History(View):
    '''历史房价接口'''

    def __init__(self, **kwargs):
        '''
        获得城市英文到中文的映射表
        :param kwargs:
        '''
        with open("./house/city_mapping_e2c.pkl", "rb") as f:
            self.city_mapping = pickle.load(f)

    def get(self, request, city):
        '''

        :param request: 请求对象
        :param city: 要获取哪个城市的历史房价信息，英文
        :return: 返回 last_n_month 个月的历史价格
        '''
        # 检查是否有该城市
        location = self.city_mapping.get(city, None)
        if location is None:
            return JsonResponse({'code': 1, 'msg': "没有这个城市"})

        # 检查 '最近n月' 是否合法
        try:
            last_n_month = int(float(request.GET.get("last_n_month", 6)))

            if last_n_month <= 0:
                raise ValueError
        except ValueError:
            return JsonResponse({'code': 2, 'msg': "不合法的年份信息"})

        # 查询数据库
        past_prices = HistoryPrice.objects.filter(location=location).order_by("-year", "-month")[:last_n_month]

        count = len(past_prices)  # 检索到的有效记录数
        prices = []
        for price in past_prices[::-1]:  # 数据汇总
            prices.append(['{}-{}'.format(price.year, price.month), str(price.average_price), str(price.tendency)])

        return JsonResponse({"code": 0, "count": count, "city": location, "data": prices})  # 返回 Json 响应

    def post(self):
        pass


# url:house/price/<city>/sub_location/
class CityInfoView(View):
    '''城市层级信息接口'''

    def __init__(self):
        with open("./house/city_mapping_e2c.pkl", "rb") as f:
            self.city_mapping = pickle.load(f)
        # 建立到 MongoDB 的连接， Mongodb存放城市及下级地区的映射关系
        client = MongoClient(host="42.159.122.43", port=27018)
        db = client.MBH
        self.city_relations = db.city_relations
        # 查询一次，存储在 cursor 中
        self.cursor = list(self.city_relations.find())[0]

    def get(self, request, location):
        '''
        :param request:
        :param location: 要查哪个城市的下级
        :return: 返回对应城市的所有下级(区和街道)
        '''
        # 英文转中文
        location_cn = self.city_mapping.get(location, None)
        if location_cn is None:
            return JsonResponse({"code": 1, "msg": "查询参数有误"})
        # 去数据库查询
        sub_location = self.cursor.get(location_cn, "None")
        # 返回数据
        if sub_location is None:
            return JsonResponse({"code": 2, "msg": "查无此城"})
        else:
            return JsonResponse({"code": 0, "data": sub_location}, safe=False)


# url:house/price/<city>/sub_location?year=xxxx&month=yy
class SubLocationPriceView(View):
    '''获取下级最新房价'''
    def __init__(self):
        with open("./house/city_mapping_e2c.pkl", "rb") as f:
            self.city_mapping = pickle.load(f)
            # 建立到 MongoDB 的连接
        client = MongoClient(host=settings.MONGODB_IP, port=settings.MONGODB_PORT)
        db = client.MBH
        self.city_relations = db.city_relations
        # 查询一次，存储在 cursor 中
        self.cursor = list(self.city_relations.find())[0]

    def get(self, request, city_name):
        '''
        :param request:
        :param city_name: 要获取哪个城市的下级一层房价
        :return: 房价列表 + 对应的日期列表
        '''
        location_cn = self.city_mapping.get(city_name, None)
        year = request.GET.get("year", None)
        month = request.GET.get("month", None)
        # 获取年份和月份信息
        if year is None:
            year = datetime.datetime.now().year

        if month is None:
            # 使用当前月
            cur_month = datetime.datetime.now().month
            # 格式化成数据库中存储的格式
            month = '0'+str(cur_month) if cur_month <= 9 else str(cur_month)
        else:
            if len(month) == 1:
                month = '0'+month
        if location_cn is None:
            return JsonResponse({"code": 1, "msg": "没有这个城市"})

        # 查询下属城镇信息
        subs = self.cursor.get(location_cn, None)
        if subs is None:
            return JsonResponse({"code": 2, "msg": "已经到最后一级了"})

        ret = [list()]
        date_time = list()

        for i, sub in enumerate(subs):
            sub_info = HistoryPrice.objects.filter(Q(location=sub) & Q(year=year) & Q(month=month))
            if len(list(sub_info)) == 0:
                continue
            else:
                ret[0].append([sub_info[0].location, sub_info[0].average_price])
                if len(date_time) == 0:
                    date_time.append('{}-{}'.format(sub_info[0].year, sub_info[0].month))
        return JsonResponse({"code": 0, "data": ret, "location_cn": location_cn, "time": date_time})

# url:house/price/<city>/overview?number=x
class HouseOverView(View):
    '''
    主页收藏量数据接口
    '''
    def __init__(self):
        with open("./house/city_mapping_e2c.pkl", "rb") as f:
            self.city_mapping = pickle.load(f)

    def get(self, request, city_name):
        '''
        :param request:
        :param city_name: 要获取哪个城市的收藏量
        :return: 返回前N个收藏量最多的房源，N在settings中指定
        '''
        # 连接 redis 数据库
        conn = get_redis_connection('User&House')
        city_top_key = "{}_topN".format(city_name)
        top_list = conn.zrevrangebyscore(city_top_key, sys.maxsize, 0, withscores=True, \
                                         start=0, num=settings.STAR_COUNT_TOP_N)
        top_list = [v[0].decode() for v in top_list]
        # 获取收藏量前列的房子信息
        records = House.objects.filter(id__in=top_list)
        diff_num = settings.STAR_COUNT_TOP_N - len(top_list)
        topN_infos = list()
        # 构造返回值
        for info in records:
            item = dict()
            item["id"] = info.id
            item['garden'] = info.garden
            item['description'] = info.description
            item['area'] = info.area
            item['total_price'] = info.total_price
            item['img_url'] = info.pic_url
            item['orientation'] = info.orientation
            item['layout'] = info.layout
            topN_infos.append(item)
        # 收藏量不够时，随机选，补齐
        if diff_num > 0:
            try:
                location_cn = self.city_mapping[city_name]
            except KeyError:
                return JsonResponse({"code": 1, "msg": "错误的城市信息"})
            house_city_record = House.objects.filter(city=location_cn, price__gt=0, pic_url__startswith="http")
            sample = random.sample(range(house_city_record.count()), diff_num)
            records_append = [house_city_record.all()[i] for i in sample]
            for info in records_append:
                item = dict()
                item["id"] = info.id
                item['garden'] = info.garden
                item['description'] = info.description
                item['area'] = info.area
                item['total_price'] = info.total_price
                item['img_url'] = info.pic_url
                item['orientation'] = info.orientation
                item['layout'] = info.layout
                topN_infos.append(item)

        return JsonResponse({"code": 0, "data": topN_infos, 'count': len(topN_infos)})


# url:house/price/<city>/mainpage_overview
class HouseMainPageView(View):
    '''
    首页的房价数据接口
    '''
    def __init__(self):
        with open("./house/city_mapping_e2c.pkl", "rb") as f:
            self.city_mapping = pickle.load(f)

    def get(self, request, city_name):
        '''
        :param request:
        :param city_name: 要获取房价的城市(当前定位城市)
        :return: 返回当前城市的当前月份
        '''
        location_cn = self.city_mapping.get(city_name, None)

        year = datetime.datetime.now().year

        # 使用当前月
        cur_month = datetime.datetime.now().month
        # 格式化成数据库中存储的格式
        month = '0' + str(cur_month) if cur_month <= 9 else str(cur_month)
        overview_infos = list()
        infos = HistoryPrice.objects.filter(Q(location=location_cn) & Q(year=year) & Q(month=month))
        if len(infos) < 1:
            JsonResponse({"code": 1, "msg": '该地区的信息不足'})
        for info in infos:
            overview_infos.append(info.average_price)

        return JsonResponse({"code": 0, "data": overview_infos})


# url: house/filter/<city_name>
class HouseListFilterView(View):
    '''房子列表展示的地区筛选'''
    def __init__(self):
        with open("./house/city_mapping_e2c.pkl", "rb") as f:
            self.city_mapping = pickle.load(f)

    def get(self, request, city_name):
        '''
        :param request:
        :param city_name:  要筛选的城市名，英文
        :return: 按给定条件筛选后的房源集
        '''
        location_cn = self.city_mapping.get(city_name, None)
        if location_cn is None:
            return JsonResponse({"code": 1, "msg": "查无此城市的次级信息"})

        records = House.objects.filter(city=location_cn)
        districts = records.values("district").distinct()
        districts = [district['district'] for district in districts]

        zones = dict()
        for district in districts:
            zone_queryset = records.filter(district=district).values("zone").distinct()
            zones[district] = [zone['zone'] for zone in zone_queryset]
        data = {'city': location_cn, 'districts': districts, 'zones': zones}
        return JsonResponse({"code": 0, 'data': data})


# url: house/detail/<house_id>
class HouseDetailView(View):
    '''房子详情信息接口'''

    def get(self, request, house_id):
        '''
        :param request:
        :param house_id: 要获取房源详情的 house_id
        :return: 返回指定房子的详情、浏览量、收藏量
        '''
        conn = get_redis_connection("User&House")
        try:
            session_user = json.loads(request.session['user'])
            user_id = session_user.get('id')
            user_key = "user_{}".format(user_id)

            # 检查是否已收藏
            star_list = conn.lrange(user_key, 0, -1)
            star_list = [item.decode() for item in star_list]
            if str(house_id) in star_list:
                star_flag = True
            else:
                star_flag = False
        except KeyError:
            star_flag = False

        try:
            house = House.objects.get(id=house_id)
        except House.DoesNotExist:
            return JsonResponse({"code": 1, "msg": "<{}> 不存在".format(house_id)})

        # 增加浏览量计数
        house_key = "house_{}".format(house_id)
        conn.hincrby(house_key, "view_count", 1)
        view_count = int(conn.hget(house_key, "view_count").decode())
        # 获取该房子的收藏量
        star_count = conn.hget(house_key, "star_count")
        if star_count is None:
            star_count = 0
        else:
            star_count = star_count.decode()

        # 组装返回数据
        data = dict()
        data['description'] = house.description
        data['total_price'] = house.total_price
        data['price'] = house.average_price
        data['layout'] = house.layout
        data['orientation'] = house.orientation
        data['area'] = house.area
        data['layer'] = house.layer
        data['architecture'] = house.architecture
        data['built_year'] = house.built_year
        data['garden'] = house.garden
        data['location'] = "{} {}".format(house.district, house.zone)
        data['developer'] = house.developer
        data['property_company'] = house.property_company
        data['contact'] = house.agent_contact
        data['pic_url'] = house.pic_url

        return JsonResponse({"code": 0, "data": data, "view_count": view_count, "star_count": star_count, \
                             "star_flag": star_flag})


# url: house/list/<city>?page_num =zz&district=xx&zone=yy
class HouseListView(View):
    '''房源列表接口'''

    def __init__(self):
        with open("./house/city_mapping_e2c.pkl", "rb") as f:
            self.city_mapping = pickle.load(f)

    def get(self, request, city_name):
        '''
        :param request:
        :param city_name: 要获取哪个城市(中文名)的房子列表
        :return: 第 page_num 页的房源列表，以及符合条件的总个数
        '''
        # 转成中文城市名
        decoded_location = self.city_mapping.get(city_name, None)
        try:
            # 先查询该城市且有价格的记录
            house_list = House.objects.filter(Q(city=decoded_location) & ~Q(price=0))
        except:
            return JsonResponse({"code": 1, "msg": "城市信息有误"})

        # 检查页码参数
        page_num = request.GET.get('page_num', None)
        if page_num is None:
            page_num = 1
        else:
            try:
                page_num = int(float(page_num))
            except TypeError:
                return JsonResponse({"code": 1, "msg": "页码格式不合法！"})

        # 链接redis数据库
        conn = get_redis_connection("User&House")
        collection_infos = list()

        # 对结果分页
        pageinator = Paginator(house_list, settings.LIST_PAGE_ITEMS)
        total_item_num = pageinator.count
        # 检索指定页数据, 构造返回值
        for house_obj in pageinator.page(page_num).object_list:
            house_info = dict()
            house_key = "house_{}".format(house_obj.id)
            star_count = conn.hget(house_key, "star_count")
            if star_count is None:
                star_count = 0
            else:
                star_count = star_count.decode()
            house_info["description"] = house_obj.description
            house_info["layout"] = house_obj.layout
            house_info["layer"] = house_obj.layer
            house_info["built_year"] = house_obj.built_year
            house_info["area"] = house_obj.area
            house_info["price"] = house_obj.average_price
            house_info["total_price"] = house_obj.total_price
            house_info["orientation"] = house_obj.orientation
            house_info["garden"] = house_obj.garden
            house_info["developer"] = house_obj.developer
            house_info["architecture"] = house_obj.architecture
            house_info["id"] = house_obj.id
            house_info["img_url"] = house_obj.pic_url
            house_info["star_count"] = star_count
            collection_infos.append(house_info)

        return JsonResponse({"code": 0, "data": collection_infos, 'total_item_num': total_item_num})


# url: house/filter?
class FilterView(View):
    '''条件查询接口'''
    def __init__(self):
        self.conn=get_redis_connection("User&House")

    def post(self, request):
        '''
        :param request:
        :return: 符合条件的结果集
        '''
        # 获取过滤条件和页码
        data = json.loads(request.body)
        city = data.get('city', None)
        area = data.get('area', None)
        price = data.get('price', None)
        layout = data.get('house', None)
        district = data.get('region', None)
        orientation = data.get('south_north', None)
        page_num = int(data.get('page', 1))
        sort = int(data.get('sort', 0))
        try:
            records = House.objects.filter(city=city)
        except House.DoesNotExist:
            return JsonResponse({"code": 2, "msg": "没有符合条件的数据"})
        # 如果选择了区， 先对区筛选
        if district != '':
            records = records.filter(district=district)
        # 对面积筛选
        area_lowbound, area_highbound = map(int, area.split('~'))
        if area_highbound == area_lowbound:
            if area_lowbound == 200:
                # 200 以上
                records = records.filter(area__gte=200)
        else:
            records = records.filter(Q(area__gt=area_lowbound) & Q(area__lt=area_highbound))

        # 对总价筛选
        price_lowbound, price_highbound = map(int, price.split('~'))
        if price_lowbound == price_highbound:
            if price_lowbound == 500:
                records = records.filter(total_price__gte=500)
        else:
            records = records.filter(Q(total_price__gt=price_lowbound) & Q(total_price__lt=price_highbound))

        # 对朝向筛选
        if orientation:
            records = records.filter(Q(orientation__contains="南") | Q(orientation__contains="北"))

        # 对户型筛选
        # 过滤掉没有户型信息的数据
        records = records.filter(layout__contains='室')
        layout = int(layout)
        if layout == 6:
            # 5室以上
            pass
        if layout in list(range(1, 6)):
            # 1-5室
            records = records.filter(layout__startswith=str(layout))

        # 排序相关
        if sort == 1:
            # 按单价降序
            records = records.order_by("-average_price")
        elif sort == 2:
            # 按单价升序
            records = records.order_by("average_price")
        elif sort == 3:
            # 按总价降序
            records = records.order_by("-total_price")
        elif sort == 4:
            # 按总价升序
            records = records.order_by("total_price")
        elif sort == 5:
            # 按面积降序
            records = records.order_by("-area")
        elif sort == 6:
            # 按面积升序
            records = records.order_by("area")

        # 分页
        page = Paginator(records, settings.LIST_PAGE_ITEMS)
        collections = list()
        # 构造返回值
        for house_obj in page.page(page_num):
            # 返回第 page_num 页内容
            house_info = dict()

            house_key = "house_{}".format(house_obj.id)
            star_count = self.conn.hget(house_key, "star_count")
            if star_count is None:
                star_count = 0
            else:
                star_count = star_count.decode()
            house_info["description"] = house_obj.description
            house_info["layout"] = house_obj.layout
            house_info["layer"] = house_obj.layer
            house_info["built_year"] = house_obj.built_year
            house_info["area"] = house_obj.area
            house_info["price"] = house_obj.average_price
            house_info["total_price"] = house_obj.total_price
            house_info["orientation"] = house_obj.orientation
            house_info["garden"] = house_obj.garden
            house_info["developer"] = house_obj.developer
            house_info["architecture"] = house_obj.architecture
            house_info["id"] = house_obj.id
            house_info["img_url"] = settings.DEFAULT_HOUSE_PIC_URL \
                                    if house_obj.pic_url == "暂无房屋图片" else house_obj.pic_url
            house_info["star_count"] = star_count
            collections.append(house_info)
        return JsonResponse({"code": 0, "data": collections, \
                             'total_item_num': page.count})

# 搜索接口的相关包
from drf_haystack.viewsets import HaystackViewSet
from .serializers import HouseIndexSerializer, StandardResultSetPagination

# 搜索结果的视图
class HouseSearchViewSet(HaystackViewSet):
    index_models = [House]
    serializer_class = HouseIndexSerializer
    pagination_class = StandardResultSetPagination

# url: house/news/<city_name>
class GetNewsInfo(View):
    '''
    获取新闻信息接口
    '''
    def get(self, request, city_name):
        '''
        :param request:
        :param city_name: 要查询哪个城市的新闻，中文
        :return: 返回前4条新闻
        '''
        news_items = News.objects.filter(city=city_name).order_by("-pub_date")[:4]
        news_collection = list()

        for item in news_items:
            news_info = dict()
            news_info['title'] = item.title
            news_info['body'] = item.body
            news_info['source'] = item.source
            news_info['pub_date'] = item.pub_date
            news_collection.append(news_info)

        return JsonResponse({"code": 0, "data": news_collection, "count": len(news_collection)})


# url: house/predict/<city_name>
class PredictPriceView(View):
    '''
    获取预测价格
    '''
    def __init__(self):
        with open("./house/city_mapping_e2c.pkl", "rb") as f:
            self.city_mapping = pickle.load(f)

    def get_timepoint(self, month_gap=0):
        '''
        以当前月为准，按月份相加减
        :param month_gap: 找几个月
        :return: 符合条件的 {'year': year, 'month': month}
        '''
        cur_datetime = datetime.datetime.now()
        offset_datetime = cur_datetime + relativedelta(months=month_gap)
        month = offset_datetime.month

        # 把月份调整成符合数据库中的数据格式
        month = str(month) if month > 9 else '0' + str(month)
        return {'year': offset_datetime.year, 'month': month}

    def get(self, request, city_name):
        '''
        :param request:
        :param city_name: 哪个城市的预测房价
        :return:
        '''
        city_cn = self.city_mapping.get(city_name, None)
        if city_cn is None:
            return JsonResponse({"code": 1, "msg": "城市有误"})

        # 先过滤掉无关城市记录
        predict_records = PredictPrice.objects.filter(location=city_cn)
        history_records = HistoryPrice.objects.filter(location=city_cn)
        # 获取指定的时间点，来自表格里的日期
        current = self.get_timepoint()
        one_month_before = self.get_timepoint(month_gap=-1)
        half_year_before = self.get_timepoint(month_gap=-6)
        one_month_after = self.get_timepoint(month_gap=1)
        three_month_after = self.get_timepoint(month_gap=3)
        # 历史和未来
        history_timepoints = [half_year_before, one_month_before, current]
        predict_timepoints = [one_month_after, three_month_after]
        # 分表查询
        ret = list()
        for timepoint in history_timepoints:
            try:
                entry = history_records.get(Q(year=timepoint['year']) & Q(month=timepoint['month']))
            except:
                return JsonResponse({"code": 2, "msg": "查不到该时间的历史价格"})
            else:
                ret.append(entry.average_price)

        for timepoint in predict_timepoints:
            try:
                entry = predict_records.get(Q(year=timepoint['year']) & Q(month=timepoint['month']))
            except:
                return JsonResponse({"code": 3, "msg": "查不到该时间的预测价格"})
            else:
                ret.append(entry.predict_price)

        # 获取前6后3的数据，用于趋势图
        last_6_timepoints = list()
        for i in range(1, 7):  # [1, 2, 3, 4, 5, 6]
            last_6_timepoints.append(self.get_timepoint(month_gap=i-6))

        fore_3_timepoints = list()
        for i in range(3):
            fore_3_timepoints.append(self.get_timepoint(month_gap=i+1))

        chart_data = list()
        # 到历史房价结果集中找
        for timepoint in last_6_timepoints:
            try:
                 entry = history_records.get(year=timepoint['year'], month=timepoint['month'])
            except:
                # 找不到当前时间点的记录，则跳过，查找下一个
                continue
            else:
                chart_data.append(["{}-{}".format(timepoint["year"], timepoint["month"]), entry.average_price])
        # 到预测结果集中找
        for timepoint in fore_3_timepoints:
            try:
                entry = predict_records.get(year=timepoint['year'], month=timepoint['month'])
            except:
                continue
            else:
                chart_data.append(["{}-{}".format(timepoint["year"], timepoint["month"]), entry.predict_price])

        # 计算当前月的实际房价和预测房价的误差
        cur_year, cur_month = last_6_timepoints[5]['year'], last_6_timepoints[5]['month']
        cur_predict_price = predict_records.get(year=cur_year, month=cur_month).predict_price
        cur_real_price = history_records.get(year=cur_year, month=cur_month).average_price
        error = int(cur_real_price) - int(cur_predict_price)

        return JsonResponse({"code": 0, "data": ret, "count": len(ret), 'chart_data': chart_data, 'error': error})