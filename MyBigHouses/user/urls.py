from django.conf.urls import url
from .views import login
app_name = 'user'

urlpatterns = [
    url('login', login, name='login')
]