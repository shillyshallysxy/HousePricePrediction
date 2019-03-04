from django.shortcuts import render, redirect,reverse
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from .models import User
import json
from hashlib import md5  # 加密密码
from django.conf import settings
from django.middleware.csrf import get_token, rotate_token
from celery_task.tasks import send_activate_email  # 发送邮件函数
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature  # 加密 激活URL
from django.views.decorators.csrf import csrf_exempt
import datetime
# Create your views here.

# url: /user/login/
class LoginView(View):
    '''登录类视图'''

    def get(self, request):
        # method == 'GET'
        get_token(request)
        return JsonResponse({})

    def post(self, request):
        # get_token(request)
        data = json.loads(request.body)
        username = data["username"]
        pwd = data["password"]
        try:
            user = User.objects.get(username=username)
        except:
            return JsonResponse({'code': 5, 'msg': u'该用户名不存在！'})
        if user:
            pwd_correct = user.password
            if md5(pwd.encode('utf-8')).hexdigest() == pwd_correct:
                if user.is_active:
                    request.session['user'] = object_to_json(user)
                    return HttpResponse('登陆成功!')
                else:
                    # 未激活
                    return JsonResponse({'code': 3, 'msg': u'账户未激活！'})
            else:
                # 密码错误
                return JsonResponse({'code': 4, 'msg': u'密码错误！'})
        else:
            # username不存在
            return JsonResponse({'code': 5, 'msg': u'该用户名不存在！'})


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


# url: /user/active/<id>
class ActiveView(View):
    def get(self, request, token):
        print(token)
        serializer = Serializer(settings.SECRET_KEY, 3600)

        try:
            info = serializer.loads(token)
        except SignatureExpired as e:
            return HttpResponse('该链接已过期')
        except BadSignature as e:
            return HttpResponse('不合法的激活链接')

        user_id = info['confirm']
        user = User.objects.get(id=user_id)
        user.is_active = 1  # 激活成功
        user.save()
        # 激活成功，重定向到登录页面
        # return redirect(reverse('login'))
        return HttpResponse("您已激活成功")



# url: /user/register/
class RegisterView(View):
    '''注册类视图'''

    def get(self, request):
        get_token(request)
        return render(request, 'register.html')

    def post(self, request):
        # 接受数据
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        # form_data = json.loads(request.body)
        # username = form_data.get('username')
        # password = form_data.get('password')
        # email = form_data.get('email')

        # 检查是否重名
        try:
            user = User.objects.get(username=username)
        except:
            user = None

        if user:
            return JsonResponse({'code': 1, "msg": "用户名已存在"})

        # 检查邮箱是否被占用
        try:
            user = User.objects.get(email=email)
        except:
            user = None
        if user:
            return JsonResponse({"code": 2, "msg": "邮箱已经被占用"})

        user = User()
        user.username = username
        user.email = email
        user.password = md5(password.encode('utf-8')).hexdigest()  # 存储密码的MD5
        user.is_active = 0  # 默认未激活
        user.save()

        # 发送验证邮件
        serialier = Serializer(settings.SECRET_KEY, 3600)  # 过期时间 3600s
        info = {'confirm': user.id}
        token = serialier.dumps(info).decode()

        # 向 celery 发送邮件任务
        send_activate_email.delay(email, username, token)

        # 重定向到登录页面
        # return redirect(reverse('login'))
        return HttpResponse("注册成功! 请查看邮箱以激活账号")

