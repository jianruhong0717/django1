from django.contrib import admin
from models import *
# Register your models here.


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'ttitle']

admin.site.register(TypeInfo, TypeAdmin)


class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'gtitle']

admin.site.register(GoodsInfo, GoodsAdmin)
