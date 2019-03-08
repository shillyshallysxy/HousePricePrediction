from django.http import HttpResponse, JsonResponse
from .models import House, HistoryPrice
from django.views.generic import View
import pickle
# Create your views here.


# url: /history/<city>?last_n_month=xx
class History(View):
    '''历史房价接口'''

    def __init__(self, **kwargs):
        with open("./house/city_mapping.pkl", "rb") as f:
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
        for price in past_prices:  # 数据汇总
            prices.append([price.year, price.month, str(price.average_price), str(price.tendency)])

        return JsonResponse({"code": 0, "count": count, "data": prices})  # 返回 Json 响应

    def post(self):
        pass