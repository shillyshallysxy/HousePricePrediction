from django.conf.urls import url
from .views import RegisterView, ActiveView, LoginView, UploadAvatarView, StarCountView, GetAvatarView
app_name = 'user'

urlpatterns = [
    url(r'register/', RegisterView.as_view(), name="register"),
    url(r'active/(?P<token>.*)', ActiveView.as_view(), name='active'),
    url('login', LoginView.as_view(), name='login'),
    url(r'modify_avatar', UploadAvatarView.as_view(), name="modify_avatar"),
    url(r'get_avatar', GetAvatarView.as_view(), name="get_avatar"),
    url(r'star', StarCountView.as_view(), name="manage_star"),
]