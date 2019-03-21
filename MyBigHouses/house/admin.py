from django.contrib import admin
from .models import House, HistoryPrice, News
# Register your models here.

# 注册到后台管理界面
admin.site.register(House)
admin.site.register(HistoryPrice)
admin.site.register(News)