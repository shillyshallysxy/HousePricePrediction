# 登录检查装饰器
from django.http.response import JsonResponse


def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.has_key('user'):
            return view_func(request, *args, **kwargs)
        else:
            return JsonResponse({"code": 1, 'msg': "请您先登录~"})
    return wrapper