# Generated by Django 2.2 on 2020-03-19 19:08

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=24, verbose_name='品牌')),
            ],
            options={
                'verbose_name': '品牌',
                'verbose_name_plural': '品牌',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='供应商')),
                ('tel', models.CharField(max_length=24, verbose_name='公司电话')),
                ('contact', models.CharField(max_length=64, verbose_name='联系人')),
                ('phone', models.CharField(max_length=13, verbose_name='联系手机')),
            ],
            options={
                'verbose_name': '供应商',
                'verbose_name_plural': '供应商',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('Gmodel', models.CharField(max_length=64, unique=True, verbose_name='品名规格')),
                ('unit', models.IntegerField(choices=[(0, '台'), (1, '支'), (2, '个'), (3, '站点'), (4, '用户'), (5, '套'), (6, 'PCS')], verbose_name='单位')),
                ('type', models.IntegerField(choices=[(0, '条码打印机'), (1, '条码扫描器'), (2, '数据终端'), (3, '软件'), (4, '配件'), (5, '耗材'), (6, 'RFID设备'), (7, '其它')], verbose_name='分类')),
                ('price', models.FloatField(default=0, verbose_name='进价')),
                ('min_price', models.FloatField(default=0, verbose_name='最低价')),
                ('meno', models.TextField(default='备注信息', verbose_name='备注')),
                ('date', models.DateField(auto_now=True, verbose_name='更改日期')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.Brand', verbose_name='品牌')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='list.Supplier', verbose_name='供应商')),
            ],
            options={
                'verbose_name': '产品',
                'verbose_name_plural': '产品信息',
            },
        ),
    ]
