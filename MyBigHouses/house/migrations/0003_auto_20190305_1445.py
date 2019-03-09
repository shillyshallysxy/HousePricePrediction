# Generated by Django 2.1.7 on 2019-03-05 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0002_auto_20190305_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='description',
            field=models.CharField(default='暂无该房源的描述', max_length=100, null=True, verbose_name='房子描述'),
        ),
        migrations.AlterField(
            model_name='house',
            name='developer',
            field=models.CharField(max_length=50, null=True, verbose_name='开发商'),
        ),
        migrations.AlterField(
            model_name='house',
            name='orientation',
            field=models.CharField(default='暂无朝向信息', max_length=20, null=True, verbose_name='朝向'),
        ),
        migrations.AlterField(
            model_name='house',
            name='property_company',
            field=models.CharField(max_length=50, null=True, verbose_name='物业公司'),
        ),
    ]