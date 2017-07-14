# coding=utf-8
from django.db import models

# Create your models here.


class UserInfo(models.Model):
    uname = models.CharField(max_length=20)  # 用户名
    upwd = models.CharField(max_length=40)  # sha1加密
    umail = models.CharField(max_length=30)  # 注册邮箱
    uphone = models.CharField(max_length=11)  # 手机号
    ucode = models.CharField(max_length=6)  # 邮编
    ushou_name = models.CharField(max_length=20)  # 收货人
    uaddress = models.CharField(max_length=100)  # 收货地址
