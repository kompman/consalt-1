# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0010_auto_20150504_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='block12_back',
            field=models.ImageField(default=b'images/bg_1.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a12 \u0424\u043e\u043d\u043e\u0432\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block12_button_color',
            field=colorfield.fields.ColorField(default=b'#fff600', max_length=10, verbose_name='\u0411\u043b\u043e\u043a12 \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block12_button_text',
            field=models.CharField(default='\u0417\u0410\u041a\u0410\u0417\u0410\u0422\u042c \u0411\u0415\u0421\u041f\u041b\u0410\u0422\u041d\u0423\u042e \u041a\u041e\u041d\u0421\u0423\u041b\u042c\u0422\u0410\u0426\u0418\u042e', max_length=100, verbose_name='\u0411\u043b\u043e\u043a12 \u0422\u0435\u043a\u0441\u0442 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block12_image',
            field=models.ImageField(default=b'images/kak_rabotaem.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a12 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0441 \u0446\u0438\u0444\u0440\u0430\u043c\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block12_item1_text',
            field=models.CharField(default='\u0417\u0430\u043a\u0430\u0437 \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e\u0439</br>\u043a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0430\u0446\u0438\u0438', max_length=200, verbose_name='\u0411\u043b\u043e\u043a12 \u0422\u0435\u043a\u0441\u0442 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block12_item2_text',
            field=models.CharField(default='\u0413\u043e\u0442\u043e\u0432\u0438\u043c \u0434\u043b\u044f \u0412\u0430\u0441 \u043f\u043e\u0448\u0430\u0433\u043e\u0432\u044b\u0439</br>\u043f\u043b\u0430\u043d \u0440\u0435\u0448\u0435\u043d\u0438\u044f \u0437\u0430\u0434\u0430\u0447\u0438', max_length=200, verbose_name='\u0411\u043b\u043e\u043a12 \u0422\u0435\u043a\u0441\u0442 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block12_item3_text',
            field=models.CharField(default='\u041f\u043e\u043b\u0443\u0447\u0430\u0435\u043c</br>\u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442', max_length=200, verbose_name='\u0411\u043b\u043e\u043a12 \u0422\u0435\u043a\u0441\u0442 \u0442\u0440\u0435\u0442\u044c\u0435\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block12_item4_text',
            field=models.CharField(default='\u041d\u0430\u0448\u0430 \u043a\u043e\u043c\u0430\u043d\u0434\u0430 \u0430\u043d\u0430\u043b\u0438\u0437\u0438\u0440\u0443\u0435\u0442</br>\u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044e', max_length=200, verbose_name='\u0411\u043b\u043e\u043a12 \u0422\u0435\u043a\u0441\u0442 \u0447\u0435\u0442\u0432\u0435\u0440\u043d\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block12_item5_text',
            field=models.CharField(default='\u0421\u043e\u0433\u043b\u0430\u0441\u043e\u0432\u044b\u0432\u0430\u0435\u043c \u0443\u0441\u043b\u043e\u0432\u0438\u0435</br>\u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u0447\u0435\u0441\u0442\u0432\u0430', max_length=200, verbose_name='\u0411\u043b\u043e\u043a12 \u0422\u0435\u043a\u0441\u0442 \u0447\u0435\u0442\u0432\u0435\u0440\u043d\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block12_text',
            field=models.CharField(default='\u041a\u0410\u041a \u041c\u042b \u0420\u0410\u0411\u041e\u0422\u0410\u0415\u041c', max_length=100, verbose_name='\u0411\u043b\u043e\u043a12 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
    ]
