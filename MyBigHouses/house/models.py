from django.db import models
from tinymce.models import HTMLField

# Create your models here.

class House(models.Model):
    '''住房详细信息类'''

    date = models.DateField(auto_now_add=True, verbose_name="创建时间")
    city = models.CharField(max_length=20, null=False, verbose_name="城市")
    district = models.CharField(max_length=20, null=True, verbose_name="县")
    zone = models.CharField(max_length=20, null=True, verbose_name="区")
    garden = models.CharField(max_length=40, null=True, verbose_name="小区")
    architecture = models.CharField(max_length=30, null=True, verbose_name="版型")
    property_fee = models.CharField(max_length=30, null=True, verbose_name="物业费")
    property_company = models.CharField(max_length=50, null=True, verbose_name="物业公司")
    developer = models.CharField(max_length=50, null=True, verbose_name="开发商")
    average_price = models.IntegerField(verbose_name="小区均价")
    on_sale = models.IntegerField(verbose_name="在售房数量")

    description = models.CharField(max_length=100, null=True, default="暂无该房源的描述", verbose_name="房子描述")
    layout = models.CharField(max_length=20, null=True, default="此房暂时不在售", verbose_name="房型")
    layer = models.CharField(max_length=30, null=True, default="暂无楼层信息",verbose_name="楼层")
    built_year = models.CharField(max_length=8, null=True, default="年份未知", verbose_name="建造年份")
    area = models.DecimalField(decimal_places=1, max_digits= 10,null=True, default=0.0, verbose_name="住房面积")
    price = models.DecimalField(decimal_places=1, max_digits= 10, null=True, default=0.0, verbose_name="住房单价")
    total_price = models.DecimalField(decimal_places=2, max_digits= 13, null=True, default=0.0, verbose_name="房屋总价")
    orientation = models.CharField(max_length=20, null=True,default="暂无朝向信息",verbose_name="朝向")
    source_url = models.CharField(max_length=100, null=True, default="暂无来源", verbose_name="数据源")

    pic_url = models.URLField(max_length=100, null=True, verbose_name="图片URL")
    agent_name = models.CharField(max_length=5, null=True, verbose_name="经纪人")
    agent_contact = models.CharField(max_length=20, null=True, verbose_name="经纪人联系方式")
    layout_img_url = models.URLField(max_length=100, null=True, verbose_name="户型图片URL")
    detail = models.CharField(max_length=300, null=True, verbose_name="详细信息")
    visit_frequency = models.CharField(max_length=50, null=True, verbose_name="看房频率")

    class Meta:
        db_table = "House"
        verbose_name = "住房"
        verbose_name_plural = verbose_name

    def __str__(self):
        if len(str(self.description)) > 10:
            return self.description[:10]
        else:
            return self.description


class HistoryPrice(models.Model):
    '''历史房均价'''

    location = models.CharField(max_length=30, null=False, verbose_name="地点")
    year = models.CharField(max_length=8, null=False, verbose_name="房价年份")
    month = models.CharField(max_length=4, null=False, verbose_name="房价月份")
    average_price = models.DecimalField(max_digits=10, decimal_places=1, verbose_name="均价")
    tendency = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="增长比")

    class Meta:
        db_table = "HistoryPrice"
        verbose_name = "历史房均价"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.location


class News(models.Model):
    city = models.CharField(max_length=10, null=False, verbose_name="城市")
    add_date = models.DateField(auto_now_add=True, verbose_name="添加时间")
    pub_date = models.DateField(null=True, verbose_name="发布时间")
    title = models.CharField(max_length=30, null=True, verbose_name="新闻标题")
    body = HTMLField(blank=True, verbose_name="新闻内容")
    source = models.CharField(max_length=20, verbose_name="新闻来源")

    class Meta:
        db_table = "News"
        verbose_name = "新闻"
        verbose_name_plural = verbose_name

class PredictPrice(models.Model):
    '''历史房均价'''

    location = models.CharField(max_length=30, null=False, verbose_name="地点")
    year = models.CharField(max_length=8, null=False, verbose_name="房价年份")
    month = models.CharField(max_length=4, null=False, verbose_name="房价月份")
    predict_price = models.DecimalField(max_digits=10, decimal_places=1, verbose_name="预测的均价")

    class Meta:
        db_table = "PredictPrice"
        verbose_name = "预测房价表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.location