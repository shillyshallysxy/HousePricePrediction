from django.conf.urls import url
from django.views.generic import TemplateView
from .views import History, CityInfoView, SubLocationPriceView, HouseOverView, HouseListFilterView, HouseDetailView

app_name = 'house'

urlpatterns = [
    url(r'price/(?P<city>(\w*?))/history', History.as_view(), name="history_price"),
    url(r'city_info/(?P<location>.*)', CityInfoView.as_view(), name="city_info"),
    url(r'price/(?P<city_name>(\w*?))/sub_location', SubLocationPriceView.as_view(), name="sub_price"),
    url(r'price/(?P<city_name>(\w*?))/overview', HouseOverView.as_view(), name="house_overview"),
    url(r'list/(?P<city_name>.*)', HouseListFilterView.as_view(), name="house_list_filter"),
    url(r'detail/(?P<house_id>\d+)', HouseDetailView.as_view(), name="house_detail")
]