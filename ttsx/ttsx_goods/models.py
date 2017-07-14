# coding=utf-8
from django.db import models
from tinymce.models import HTMLField

# Create your models here.


class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)  # 商品分类
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.ttitle.encode('utf-8')


class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)  # 商品名字
    gpic = models.ImageField(upload_to='goods/')  # 图片上传路径
    gpirce = models.DecimalField(max_digits=5, decimal_places=2)  # 价格共五位数，包括两位小数
    gclick = models.IntegerField()  # 商品人气，这里按点击量来算
    gunit = models.CharField(max_length=20)  # 单位（）
    isDelete = models.BooleanField(default=False)
    gsubtitle = models.CharField(max_length=200)  # 商品描述
    gkucun = models.IntegerField(default=100)  # 默认商品库存为100
    gcontent = HTMLField()  # 商品详情介绍(通过富文本编辑器实现)
    gtype = models.ForeignKey('TypeInfo')
