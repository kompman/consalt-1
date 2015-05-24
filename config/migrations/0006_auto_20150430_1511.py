# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0005_auto_20150430_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='block3_image',
            field=models.ImageField(default=b'images/decoration_1.jpg', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a3 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u043e\u0434 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u043c', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block4_back_color',
            field=colorfield.fields.ColorField(default=b'#fff600', max_length=10, verbose_name='\u0411\u043b\u043e\u043a4 \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block4_button_color',
            field=colorfield.fields.ColorField(default=b'#fff600', max_length=10, verbose_name='\u0411\u043b\u043e\u043a4 \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block4_button_text',
            field=models.CharField(default='\u041f\u041e\u041b\u0423\u0427\u0418\u0422\u042c \u0411\u0415\u0421\u041f\u041b\u0410\u0422\u041d\u041e', max_length=100, verbose_name='\u0411\u043b\u043e\u043a4 \u0422\u0435\u043a\u0441\u0442 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block4_field_color',
            field=colorfield.fields.ColorField(default=b'#fff600', max_length=10, verbose_name='\u0411\u043b\u043e\u043a4 \u0426\u0432\u0435\u0442 \u043f\u043e\u043b\u0435\u0439', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block4_text',
            field=models.CharField(default='\u0423\u0427\u0410\u0421\u0422\u0412\u0423\u0419\u0422\u0415 \u0412 \u0410\u041a\u0426\u0418\u0418</br><span>\u0438 \u0412\u0430\u0448 \u0431\u0438\u0437\u043d\u0435\u0441 \u0432\u044b\u0439\u0434\u0435\u0442</br>\u043d\u0430 \u043d\u043e\u0432\u044b\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c!</span>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a4 \u0422\u0435\u043a\u0441\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block4_under_button_text',
            field=models.CharField(default='\u0412\u0430\u0448\u0438 \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438</br>\u0438 \u043d\u0435 \u0431\u0443\u0434\u0443\u0442 \u043f\u0435\u0440\u0435\u0434\u0430\u043d\u044b \u0442\u0440\u0435\u0442\u044c\u0438\u043c \u043b\u0438\u0446\u0430\u043c', max_length=100, verbose_name='\u0411\u043b\u043e\u043a4 \u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u043b\u0435 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block3_text',
            field=models.CharField(default='\u0422\u041e\u041b\u042c\u041a\u041e \u0421\u0415\u0413\u041e\u0414\u041d\u042f!</br>\u0412\u044b \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u0442\u0435<span> \u0411\u0415\u0421\u041f\u041b\u0410\u0422\u041d\u041e!</span>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a3 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
    ]
