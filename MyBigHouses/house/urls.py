from django.conf.urls import url, include
from django.urls import path
from django.views.generic import TemplateView
from .views import History, CityInfoView, SubLocationPriceView, HouseOverView, HouseListFilterView,\
                    HouseDetailView, HouseMainPageView, HouseListView, HouseSearchViewSet,FilterView
from rest_framework.routers import DefaultRouter

app_name = 'house'

urlpatterns = [
    url(r'price/(?P<city>(\w*?))/history', History.as_view(), name="history_price"),
    url(r'city_info/(?P<location>.*)', CityInfoView.as_view(), name="city_info"),
    url(r'price/(?P<city_name>(\w*?))/sub_location', SubLocationPriceView.as_view(), name="sub_price"),
    url(r'price/(?P<city_name>(\w*?))/overview', HouseOverView.as_view(), name="house_overview"),
    url(r'filter/(?P<city_name>.*)', HouseListFilterView.as_view(), name="house_list_filter"),
    url(r'detail/(?P<house_id>\d+)', HouseDetailView.as_view(), name="house_detail"),
    url(r'price/(?P<city_name>(\w*?))/mainpage_overview', HouseMainPageView.as_view(), name="mainpage_overview"),
    url(r'list/(?P<city_name>.*)', HouseListView.as_view(), name='list'),
	url(r'filter',FilterView.as_view(), name="filter"),
    # url(r'search/', HouseSearchViewSet, name="search")  # 搜索路由
	
]

router = DefaultRouter()
router.register(r'search', HouseSearchViewSet, base_name='house_search')
urlpatterns += router.urls
