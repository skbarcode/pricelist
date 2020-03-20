# -*- coding:utf-8 -*-
# @FileName  :adminx.py
# @Time      :2020-02-23 18:56
# @Author    :Alex Liu
import xadmin
from xadmin import views
from apps.list.models import Supplier, Goods, Brand
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin


class GlobalSittings(object):
    # global_search_models = ['Gmodel']
    site_title = '斯康后台管理系统'
    site_footer = '斯康在线网'
    menu_style = 'accordion'


class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


class GoodsResources(resources.ModelResource):
    class Meta:
        model = Goods
        skip_unchanged = True
        exclude = ('data',)
        fields = (

        )
        export_order = ('id', 'brand', 'Gmodel', 'unit', 'type', 'price', 'min_price',  'meno', 'date', 'supplier')



class GoodsAdmin(ImportExportActionModelAdmin):

    list_display = (
    'id', 'brand', 'Gmodel', 'unit', 'type', 'price', 'min_price',  'meno', 'date', 'supplier')
    search_fields = ('Gmodel','meno')
    list_display_links = ('id', 'brand', 'Gmodel',)
    list_filter = ('brand', 'type')
    list_per_page = 15
    resource_class = GoodsResources


# class GoodsAdmin(object):
#     list_display =['Gmodel', 'unit', 'type', 'price', 'min_price', 'meno',  'supplier']


class SupplierAdmin(object):
    list_display = ['id', 'name', 'tel', 'phone', 'contact', ]
    search_fields = ['name', 'contact']
    list_filter = ['name', 'contact']
    # list_editable =['name','desc']


class BrandAdmin(object):
    list_display = ['id', 'name', ]
    search_fields = ['name', ]
    list_filter = ['name', 'add_time']
    list_editable = ['name', ]


xadmin.site.register(Supplier, SupplierAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(Brand, BrandAdmin)
xadmin.site.register(xadmin.views.CommAdminView, GlobalSittings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)
