from django.http import HttpResponse, JsonResponse
from .models import House, HistoryPrice
from django.views.generic import View
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings
import pickle
from pymongo import MongoClient
from django_redis import get_redis_connection
import datetime
import json
import base64
from haystack.generic_views import SearchView
from drf_haystack.serializers import HaystackSerializer

# url: house/price/<city>/history?last_n_month=xx
class History(View):
    '''历史房价接口'''

    def __init__(self, **kwargs):
        with open("./house/city_mapping_e2c.pkl", "rb") as f:
            self.city_mapping = pickle.load(f)

    def get(self, request, city):
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
            # 建立到 MongoDB 的连接
        client = MongoClient(host="42.159.122.43", port=27018)
        db = client.MBH
        self.city_relations = db.city_relations
        # 查询一次，存储在 cursor 中
        self.cursor = list(self.city_relations.find())[0]

    def get(self, request, location):
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


# url:house/price/<city>/sub_location?last_n_month=n
# class SubLocationPriceView(View):
#     '''获取下级最新房价'''
#
#     def __init__(self):
#         with open("./house/city_mapping_e2c.pkl", "rb") as f:
#             self.city_mapping = pickle.load(f)
#             # 建立到 MongoDB 的连接
#         client = MongoClient(host="42.159.122.43", port=27018)
#         db = client.MBH
#         self.city_relations = db.city_relations
#         # 查询一次，存储在 cursor 中
#         self.cursor = list(self.city_relations.find())[0]
#
#     def get(self, request, city_name):
#         location_cn = self.city_mapping.get(city_name, None)
#         last_month = int(request.GET.get('last_n_month', 1))
#         if location_cn is None:
#             return JsonResponse({"code": 1, "msg": "没有这个城市"})
#
#         subs = self.cursor.get(location_cn, None)
#         if subs is None:
#             return JsonResponse({"code": 2, "msg": "已经到最后一级了"})
#         ret = [list() for i in range(last_month)]
#         date_time = list()
#         print(datetime.datetime.now())
#         for i, sub in enumerate(subs):
#             sub_info = HistoryPrice.objects.filter(location=sub).order_by("-year", "-month")[:last_month] # 只要最近 last_month 个月
#             if len(list(sub_info)) == 0:
#                 continue
#             else:
#                 for index in range(last_month):
#                     ret[index].append([sub_info[index].location, sub_info[index].average_price])
#                     if i == 0:
#                         date_time.append('{}-{}'.format(sub_info[index].year, sub_info[index].month))
#         print(datetime.datetime.now())
#         return JsonResponse({"code": 0, "data": ret, "location_cn": location_cn, "time": date_time})


# url:house/price/<city>/sub_location?year=xxxx&month=yy
class SubLocationPriceView(View):
    '''获取下级最新房价'''

    def __init__(self):
        with open("./house/city_mapping_e2c.pkl", "rb") as f:
            self.city_mapping = pickle.load(f)
            # 建立到 MongoDB 的连接
        client = MongoClient(host="42.159.122.43", port=27018)
        db = client.MBH
        self.city_relations = db.city_relations
        # 查询一次，存储在 cursor 中
        self.cursor = list(self.city_relations.find())[0]

    def get(self, request, city_name):
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
                if i == 0:
                    date_time.append('{}-{}'.format(sub_info[0].year, sub_info[0].month))

        return JsonResponse({"code": 0, "data": ret, "location_cn": location_cn, "time": date_time})


# url:house/price/<city>/overview?number=x
class HouseOverView(View):
    def __init__(self):
        with open("./house/city_mapping_e2c.pkl", "rb") as f:
            self.city_mapping = pickle.load(f)

    def get(self, request, city_name):
        number = request.GET.get("number", None)
        location_cn = self.city_mapping.get(city_name, None)
        # 获取年份和月份信息
        if number is None:
            number = 8
        else:
            number = int(float(number))
        overview_infos = list()
        infos = House.objects.filter(Q(city=location_cn) & ~Q(description='暂无描述') & ~Q(description='暂无该房源的描述'))[:number]
        if len(infos) < number:
            JsonResponse({"code": 1, "msg": '该地区的房源信息不足'})
        for info in infos:
            overview_infos.append({'id': info.id, 'garden': info.garden, 'description': info.description,
                                   'area': info.area, 'total_price': info.total_price,
                                   'img_url': "static/images/2.jpg"})
        return JsonResponse({"code": 0, "data": overview_infos})


# url:house/price/<city>/mainpage_overview
class HouseMainPageView(View):
    def __init__(self):
        with open("./house/city_mapping_e2c.pkl", "rb") as f:
            self.city_mapping = pickle.load(f)

    def get(self, request, city_name):
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
        data['price'] = house.price
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
        data['contact'] = '13800010001'

        return JsonResponse({"code": 0, "data": data, "view_count": view_count, "star_count": star_count, \
                             "star_flag": star_flag})


# url: house/list/<city>?page_num =zz&district=xx&zone=yy
class HouseListView(View):
    '''房源列表接口'''

    def __init__(self):
        with open("./house/city_mapping_e2c.pkl", "rb") as f:
            self.city_mapping = pickle.load(f)

    def get(self, request, city_name):
        decoded_location = self.city_mapping.get(city_name, None)
        # decoded_location = base64.b64decode(city_name).decode()
        try:
            house_list = House.objects.filter(Q(city=decoded_location) & ~Q(price=0))
        except:
            return JsonResponse({"code": 1, "msg": "城市信息有误"})
        page_num = request.GET.get('page_num', None)
        print(page_num)
        total_item_num = len(house_list)
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
        pageinator = Paginator(house_list, settings.LIST_PAGE_ITEMS)
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
            house_info["price"] = house_obj.price
            house_info["total_price"] = house_obj.total_price
            house_info["orientation"] = house_obj.orientation
            house_info["garden"] = house_obj.garden
            house_info["developer"] = house_obj.developer
            house_info["architecture"] = house_obj.architecture
            house_info["id"] = house_obj.id
            house_info["img_url"] = "static/images/2.jpg"
            house_info["star_count"] = star_count
            collection_infos.append(house_info)

        return JsonResponse({"code": 0, "data": collection_infos, 'total_item_num': len(house_list)})


#url: house/search/?q=xx
class MySearchView(SearchView):
    '''自定义搜索视图'''

    def get_queryset(self):
        queryset = super(MySearchView, self).get_queryset()
        return queryset.all()

    def get_context_data(self, *args, **kwargs):
        mySearchView = super(MySearchView, self)
        context = mySearchView.get_context_data(*args, **kwargs)
        return context

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if len(queryset) == 0:
            return JsonResponse({"code": 1, "msg": "查询结果集为空"})
        else:
            house_id_list = list()
            for item in queryset:
                house_id_list.append(item.pk)
        return JsonResponse({"code": 0, "length": len(house_id_list), "data":house_id_list})


# url: house/filter?
class FilterView(View):
    '''过滤条件'''
    def __init__(self):
        self.conn=get_redis_connection("User&House")

    def get(self, request):
        page_num = request.GET.get('page', None)

        if page_num is None:
            page_num = 1
        else:
            page_num = int(page_num)
        # 检查页码合法性
        if page_num not in self.page.page_range:
            return JsonResponse({"code": 1, "msg": "页码不合法"})

        collections = list()

        for house_obj in self.page.page(page_num):
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
            house_info["price"] = house_obj.price
            house_info["total_price"] = house_obj.total_price
            house_info["orientation"] = house_obj.orientation
            house_info["garden"] = house_obj.garden
            house_info["developer"] = house_obj.developer
            house_info["architecture"] = house_obj.architecture
            house_info["id"] = house_obj.id
            house_info["img_url"] = "static/images/2.jpg"
            house_info["star_count"] = star_count
            collections.append(house_info)

        return JsonResponse({"code": 0, "data": collections, \
                             'total_item_num': self.page.num_pages*settings.LIST_PAGE_ITEMS})

    def post(self, request):
        data = json.loads(request.body)
        city = data.get('city', None)
        area = data.get('area', None)
        price = data.get('price', None)
        layout = data.get('house', None)
        district = data.get('region', None)
        orientation = data.get('south_north', None)
        page_num = int(data.get('page', 1))
        if not all([city, area, price, layout, district, orientation]):
            return JsonResponse({'code': 1, "msg": "条件不全"})
        try:
            records = House.objects.filter(city=city)
        except House.DoesNotExist:
            return JsonResponse({"code": 2, "msg": "没有符合条件的数据"})

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
        records = records.filter(orientation__contains=orientation)

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
        # 分页
        page = Paginator(records, settings.LIST_PAGE_ITEMS)
        collections = list()

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
            house_info["price"] = house_obj.price
            house_info["total_price"] = house_obj.total_price
            house_info["orientation"] = house_obj.orientation
            house_info["garden"] = house_obj.garden
            house_info["developer"] = house_obj.developer
            house_info["architecture"] = house_obj.architecture
            house_info["id"] = house_obj.id
            house_info["img_url"] = house_obj.pic_url
            house_info["star_count"] = star_count
            collections.append(house_info)

        return JsonResponse({"code": 0, "data": collections, \
                             'total_item_num': page.num_pages*settings.LIST_PAGE_ITEM})


from drf_haystack.viewsets import HaystackViewSet
from .serializers import HouseIndexSerializer, StandardResultSetPagination


class HouseSearchViewSet(HaystackViewSet):
    index_models = [House]
    serializer_class = HouseIndexSerializer
    pagination_class = StandardResultSetPagination

