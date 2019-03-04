from django.db import models

# Create your models here.

class House(models.Model):
    '''住房详细信息类'''

    date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    city = models.CharField(max_length=20, null=False, verbose_name="城市")
    district = models.CharField(max_length=20, null=True, verbose_name="县")
    zone = models.CharField(max_length=20, null=True, verbose_name="区")
    garden = models.CharField(max_length=15, null=True, verbose_name="小区")
    architecture = models.CharField(max_length=20, null=True, verbose_name="版型")
    property_fare = models.CharField(max_length=15, null=True, verbose_name="物业费")
    property_company = models.CharField(max_length=30, null=True, verbose_name="物业公司")
    developer = models.CharField(max_length=20, null=True, verbose_name="开发商")
    average_price = models.IntegerField(verbose_name="小区均价")
    on_sale = models.IntegerField(verbose_name="在售房数量")

    description = models.CharField(max_length=50, null=True, default="暂无该房源的描述", verbose_name="房子描述")
    layout = models.CharField(max_length=10, null=True, default="此房暂时不在售", verbose_name="房型")
    layer = models.CharField(max_length=20, null=True, default="暂无楼层信息",verbose_name="楼层&年份")
    area = models.DecimalField(decimal_places=1, max_digits= 10,null=True, default=0.0, verbose_name="住房面积")
    price = models.DecimalField(decimal_places=1, max_digits= 10, null=True, default=0.0, verbose_name="住房单价")
    total_price = models.DecimalField(decimal_places=2, max_digits= 13, null=True, default=0.0, verbose_name="房屋总价")
    orientation = models.CharField(max_length=8, null=True,default="暂无朝向信息" ,verbose_name="朝向")
    source_url = models.CharField(max_length=40, null=True, default="暂无来源", verbose_name="数据源")

    class Meta:
        db_table = "House"
        verbose_name = "住房"
        verbose_name_plural = verbose_name

    def __str__(self):
        if len(str(self.description)) > 10:
            return self.description[:10]
        else:
            return self.description

