from django.conf.urls import url
from .views import RegisterView, ActiveView
from .views import login
app_name = 'user'

urlpatterns = [
    url(r'register/', RegisterView.as_view(), name="register"),
    url(r'active/(?P<token>.*)', ActiveView.as_view(), name='active'),
    url('login', login, name='login'),
]