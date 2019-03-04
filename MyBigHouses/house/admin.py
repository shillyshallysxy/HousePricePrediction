from django.contrib import admin
from .models import House
# Register your models here.

# 注册到后台管理界面
admin.site.register(House)