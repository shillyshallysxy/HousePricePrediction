from django.conf.urls import url
from django.views.generic import TemplateView
from .views import History

app_name = 'house'

urlpatterns = [
    url(r'history/(?P<city>.*)', History.as_view(), name="history_price"),
]