# 登录检查装饰器
from django.http.response import JsonResponse
from django.
import json
import datetime

def object_to_json(self):
    fields = []
    for field in self._meta.fields:
        fields.append(field.name)
    d = {}
    for attr in fields:
        if isinstance(getattr(self, attr), datetime.datetime):
            d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(getattr(self, attr), datetime.date):
            d[attr] = getattr(self, attr).strftime("%Y-%m-%d")
        else:
            d[attr] = getattr(self, attr)
        return json.dumps(d)


def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.session.has_key('user'):
            return view_func(request, *args, **kwargs)
        else:
            # return JsonResponse({"code": 1, 'msg': "请您先登录~"})
            return redirect(reverse("user:login"))
    return wrapper(view_func)