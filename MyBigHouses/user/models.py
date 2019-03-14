from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
import os
from django.conf import settings
import hashlib

# Create your models here.


def user_path_url(instance, filename):
    filename = '{}.{}'.format(hashlib.md5(filename.encode('utf-8')).hexdigest(), filename.rpartition('.')[2])
    path = "avatars/user_{0}/{1}".format(instance.id, filename)
    if os.path.exists(os.path.join(settings.MEDIA_ROOT, path)):
        os.remove(os.path.join(settings.MEDIA_ROOT, path))
    return path


class User(AbstractBaseUser, PermissionsMixin):
        username = models.CharField(max_length=20, verbose_name='用户名', unique=True)
        first_name = models.CharField(max_length=10, verbose_name='名')
        last_name = models.CharField(max_length=10, verbose_name='姓')
        email = models.EmailField(max_length=255, verbose_name='邮箱')
        avatar = models.ImageField(upload_to=user_path_url, null=True, default="avatars/default.png")
        is_active = models.BooleanField(default=True, verbose_name='是否激活')
        is_superuser = models.BooleanField(default=False, verbose_name='是否是管理员')
        is_staff = models.BooleanField(default=False)

        create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
        update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
        is_deleted = models.BooleanField(default=False, verbose_name='是否已删除')

        USERNAME_FIELD = 'username'

        REQUIRED_FIELDS = ['email']

        objects = UserManager()

        class Meta:
            db_table = 'User'
            verbose_name = '用户'
            verbose_name_plural = verbose_name

        def __str__(self):
            return self.username
