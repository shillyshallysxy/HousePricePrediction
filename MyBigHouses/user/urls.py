from django.conf.urls import url
from .views import RegisterView, ActiveView, LoginView, UploadAvatarView, StarCountView, GetInfoView
app_name = 'user'

urlpatterns = [
    # 用户注册
    url(r'register/', RegisterView.as_view(), name="register"),
    # 激活用户
    url(r'active/(?P<token>.*)', ActiveView.as_view(), name='active'),
    # 用户登录
    url('login', LoginView.as_view(), name='login'),
    # 修改用户头像
    url(r'modify_avatar', UploadAvatarView.as_view(), name="modify_avatar"),
    # 获取用户详情页信息
    url(r'get_info', GetInfoView.as_view(), name="get_info"),
    # 收藏（取消收藏）操作
    url(r'star', StarCountView.as_view(), name="manage_star"),
]