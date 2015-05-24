# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0016_auto_20150518_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block11_item1_number',
            field=models.CharField(default='7', max_length=20, verbose_name='\u0411\u043b\u043e\u043a11 \u0426\u0438\u0444\u0440\u0430 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block11_item2_number',
            field=models.CharField(default='70', max_length=20, verbose_name='\u0411\u043b\u043e\u043a11 \u0426\u0438\u0444\u0440\u0430 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block11_item3_number',
            field=models.CharField(default='4.5', max_length=20, verbose_name='\u0411\u043b\u043e\u043a11 \u0426\u0438\u0444\u0440\u0430 \u0442\u0440\u0435\u0442\u044c\u0435\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block11_item4_number',
            field=models.CharField(default='2', max_length=20, verbose_name='\u0411\u043b\u043e\u043a11 \u0426\u0438\u0444\u0440\u0430 \u0447\u0435\u0442\u0432\u0435\u0440\u0442\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block11_item5_number',
            field=models.CharField(default='45', max_length=20, verbose_name='\u0411\u043b\u043e\u043a11 \u0426\u0438\u0444\u0440\u0430 \u043f\u044f\u0442\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block14_header',
            field=models.CharField(default='\u041d\u0410\u0428\u0418 \u041f\u0410\u0420\u0422\u041d\u0415\u0420\u042b', help_text='\u041f\u0430\u0440\u0442\u043d\u0435\u0440\u043e\u0432 \u043c\u043e\u0436\u043d\u043e \u0434\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u0438\u0436\u0435', max_length=100, verbose_name='\u0411\u043b\u043e\u043a14 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
    ]
