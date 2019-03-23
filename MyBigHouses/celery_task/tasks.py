# from __future__ import absolute_import
from celery import Celery
from django.conf import settings
from django.core.mail import send_mail
import time

# # 在celery端加入
# import django
# import os
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyBigHouses.settings')
# django.setup()

# 给celery实例起个名字，redis 3 号数据库作为 broker
app = Celery('celery_task.tasks', broker="redis://42.159.122.43:6380/3")


@app.task(name='celery_task.tasks')
def send_activate_email(to_who, username, token):
    '''异步发送激活邮件'''

    subject = "<我的大房子>欢迎信息"
    message = ""
    html_msg = "<h1>{},欢迎您注册<我的大房子>会员<h1>请点击下面链接以激活账户</br>\
    <a href='http://127.0.0.1:8000/user/active/{}'>\
    http://127.0.0.1:8000/user/active/{}</a>".format(username, token,token)
    sender = settings.EMAIL_FROM
    receiver_list = [to_who]

    send_mail(subject, message, sender, receiver_list, html_message=html_msg)
    time.sleep(5)