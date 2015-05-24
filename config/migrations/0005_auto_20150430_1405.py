# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_auto_20150430_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='block2_background',
            field=models.ImageField(default=b'images/hats.jpg', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a1 \u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block2_text',
            field=models.CharField(default='\u041e\u0422\u041a\u0420\u041e\u0419\u0422\u0415 \u0421\u0412\u041e\u0419 \u041c\u0410\u0413\u0410\u0417\u0418\u041d</br><span>\u0411\u0415\u0417 \u0417\u041e\u041d\u042b \u0420\u0418\u0421\u041a\u0410!</span>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a2 \u0422\u0435\u043a\u0441\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block3_item1',
            field=models.BooleanField(default=True, verbose_name='\u0411\u043b\u043e\u043a3 \u041f\u0435\u0440\u0432\u044b\u0439 \u043f\u0443\u043d\u043a\u0442'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block3_item1_text',
            field=models.CharField(default='\u041f\u043e\u0448\u0430\u0433\u043e\u0432\u044b\u0439 \u043f\u043b\u0430\u043d \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u044f \u043c\u0438\u043d\u0438\u043c\u0430\u0440\u043a\u0435\u0442\u0430', max_length=200, verbose_name='\u0411\u043b\u043e\u043a3 \u0422\u0435\u043a\u0441\u0442 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block3_item2',
            field=models.BooleanField(default=True, verbose_name='\u0411\u043b\u043e\u043a3 \u0412\u0442\u043e\u0440\u043e\u0439 \u043f\u0443\u043d\u043a\u0442'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block3_item2_text',
            field=models.CharField(default='\u041c\u0435\u0442\u043e\u0434 \u0443\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u044f \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0447\u0435\u043a\u0430 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435', max_length=200, verbose_name='\u0411\u043b\u043e\u043a3 \u0422\u0435\u043a\u0441\u0442 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block3_item3',
            field=models.BooleanField(default=True, verbose_name='\u0411\u043b\u043e\u043a3 \u0422\u0440\u0435\u0442\u0438\u0439 \u043f\u0443\u043d\u043a\u0442'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block3_item3_text',
            field=models.CharField(default='3D \u043c\u043e\u0434\u0435\u043b\u044c \u0432\u0430\u0448\u0435\u0433\u043e \u0431\u0443\u0434\u0443\u0449\u0435\u0433\u043e \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430', max_length=200, verbose_name='\u0411\u043b\u043e\u043a3 \u0422\u0435\u043a\u0441\u0442 \u0442\u0440\u0435\u0442\u044c\u0435\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block3_list_icon',
            field=models.ImageField(default=b'images/ok.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a3 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0441\u043f\u0438\u0441\u043a\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block3_text',
            field=models.CharField(default='\u0422\u041e\u041b\u042c\u041a\u041e \u0421\u0415\u0413\u041e\u0414\u041d\u042f!</br>\u0412\u044b \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u0442\u0435<span> \u0411\u0415\u0421\u041f\u041b\u0410\u0422\u041d\u041e!</span>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a3 \u0422\u0435\u043a\u0441\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block3_time',
            field=models.TimeField(default=b'08:31:57', null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0434\u043e \u043a\u043e\u043d\u0446\u0430 \u0430\u043a\u0446\u0438\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block1_background',
            field=colorfield.fields.ColorField(default=b'#5287a7', max_length=10, verbose_name='\u0411\u043b\u043e\u043a1 \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block1_button_color',
            field=colorfield.fields.ColorField(default=b'#fff600', max_length=10, verbose_name='\u0411\u043b\u043e\u043a1 \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block1_button_text',
            field=models.CharField(default='\u0417\u0410\u041a\u0410\u0417\u0410\u0422\u042c \u0417\u0412\u041e\u041d\u041e\u041a', max_length=100, verbose_name='\u0411\u043b\u043e\u043a1 \u0422\u0435\u043a\u0441\u0442 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block1_logo',
            field=models.ImageField(default=b'images/logo.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a1 \u041b\u043e\u0433\u043e\u0442\u0438\u043f', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block1_phone',
            field=models.CharField(default='7 (918) 930-03-16', max_length=100, verbose_name='\u0411\u043b\u043e\u043a1 \u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True),
        ),
    ]
