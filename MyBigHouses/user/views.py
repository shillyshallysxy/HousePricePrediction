# encoding: utf-8


from django.shortcuts import render, redirect
from django.views.generic import View
from django.core.paginator import Paginator
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired
from django.conf import settings
from django_redis import get_redis_connection
#from celery_tasks.tasks import send_active_email
from hashlib import md5 # 加密密码
import json # 解决cookie中文乱码问题
import re
from .models import User
from django.middleware.csrf import get_token, rotate_token


# Create your views here.

def login(request):
    if request.method == 'POST':
        data = json.load(request.body)
        username = data["username"]
        pwd = data["password"]
        user = User.objects.get(username=username)
        if user:
            pwd_correct = user.password
            if md5(pwd.encode('utf-8')).hexdigest() == pwd_correct:
                if user.is_active:
                    request.session['user'] = user
                    return HttpResponse('successful login!')
                else:
                    # 未激活
                    return JsonResponse({'code': 3, 'msg': u'账户未激活！'})
            else:
                # 密码错误
                return JsonResponse({'code': 4, 'msg': u'密码错误！'})
        else:
            # username不存在
            return JsonResponse({'code': 5, 'msg': u'该用户名不存在！'})
    else:
        # method == 'GET'
        get_token(request)
        return render(request, 'login.html')


