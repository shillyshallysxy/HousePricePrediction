# !/usr/bin/python
# -*- coding: utf-8 -*-
from celery import Celery
import os
if not os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = '项目的配置路径'

# 创建celery应用
app = Celery('email')
app.config_from_object('celery_tasks.config')

# 自动注册celery任务
app.autodiscover_tasks(['celery_tasks.send_email'])
