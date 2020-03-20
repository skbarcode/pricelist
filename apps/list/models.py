from django.db import models
from apps.users.models import BaseModel


class Supplier(BaseModel):  # 供应商
    name = models.CharField(max_length=64, verbose_name='供应商', unique=True)
    tel = models.CharField(max_length=24, verbose_name='公司电话', )
    contact = models.CharField(max_length=64, verbose_name='联系人', )
    phone = models.CharField(max_length=13, verbose_name='联系手机', )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '供应商'
        verbose_name_plural = '供应商'


class Brand(BaseModel):
    name = models.CharField(max_length=24, verbose_name='品牌')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = '品牌'


class Goods(BaseModel):  # 货品资料
    brand = models.ForeignKey(to='Brand', verbose_name='品牌', on_delete=models.CASCADE)
    Gmodel = models.CharField(max_length=64, unique=True, verbose_name='品名规格')
    unit_choices = (
        (0, '台'),
        (1, '支'),
        (2, '个'),
        (3, '站点'),
        (4, '用户'),
        (5, '套'),
        (6, 'PCS'),
    )
    unit = models.IntegerField(choices=unit_choices, verbose_name='单位', )
    type_choices = (
        (0, '条码打印机'),
        (1, '条码扫描器'),
        (2, '数据终端'),
        (3, '软件'),
        (4, '配件'),
        (5, '耗材'),
        (6, 'RFID设备'),
        (7, '其它'),
    )
    type = models.IntegerField(choices=type_choices, verbose_name='分类', )

    # attribute = models.CharField(max_length=64, verbose_name='属性', blank=True, null=True)
    price = models.FloatField(verbose_name='进价', default=0)
    min_price = models.FloatField(verbose_name='最低价', default=0)
    meno = models.TextField(verbose_name='备注', default='备注信息')
    supplier = models.ForeignKey(to='Supplier', verbose_name='供应商', on_delete=models.CASCADE)
    date = models.DateField(verbose_name='更改日期', auto_now=True)

    class Meta:
        verbose_name = '产品'
        verbose_name_plural = '产品信息'

    def __str__(self):
        return self.Gmodel
