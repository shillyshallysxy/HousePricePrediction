from django.conf.urls import url
from .views import register
from django.urls import path
from .views import user
app_name = 'user'

urlpatterns = [
    url(r'^$', user)
]