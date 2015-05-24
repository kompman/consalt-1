# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0006_auto_20150430_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='block5_back',
            field=models.ImageField(default=b'images/stats.jpg', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a5 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block5_item1_text',
            field=models.CharField(default='\u041a\u0430\u0436\u0434\u044b\u0439 5 \u043e\u0442\u043a\u0440\u044b\u0432\u0430\u044e\u0449\u0438\u0439\u0441\u044f \u043c\u0430\u0433\u0430\u0437\u0438\u043d</br>\u043f\u0440\u043e\u0436\u0438\u0432\u0435\u0442 \u043d\u0435 \u0431\u043e\u043b\u0435\u0435 6 \u043c\u0435\u0441\u044f\u0446\u0435\u0432</br>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a5 \u0422\u0435\u043a\u0441\u0442 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block5_item2_text',
            field=models.CharField(default='\u041a\u0430\u0436\u0434\u044b\u0439 3 \u043c\u0430\u0433\u0430\u0437\u0438\u043d \u0434\u0430\u0441\u0442 \u043f\u0435\u0440\u0432\u0443\u044e</br>\u043f\u0440\u0438\u0431\u044b\u043b\u044c \u043d\u0435 \u0440\u0430\u043d\u0435\u0435 \u0447\u0435\u043c \u0447\u0435\u0440\u0435\u0437 8</br>\u043c\u0435\u0441\u044f\u0446\u0435\u0432', max_length=200, verbose_name='\u0411\u043b\u043e\u043a5 \u0422\u0435\u043a\u0441\u0442 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block5_item3_text',
            field=models.CharField(default='\u041a\u0430\u0436\u0434\u044b\u0439 \u0432\u0442\u043e\u0440\u043e\u0439 \u043c\u0430\u0433\u0430\u0437\u0438\u043d \u0441\u0442\u043e\u043b\u043a\u043d\u0435\u0442\u0441\u044f \u0441</br>\u043e\u0433\u0440\u043e\u043c\u043d\u043e\u0439 \u0434\u043e\u043b\u0433\u043e\u0432\u043e\u0439 \u043d\u0430\u0433\u0440\u0443\u0437\u043a\u043e\u0439</br>\u0438 \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a \u043d\u0435 \u0441\u043c\u043e\u0436\u0435\u0442 \u0437\u0430\u043a\u0440\u044b\u0442\u044c</br>\u0435\u0433\u043e \u0431\u0435\u0437 \u0443\u0431\u044b\u0442\u043a\u0430', max_length=200, verbose_name='\u0411\u043b\u043e\u043a5 \u0422\u0435\u043a\u0441\u0442 \u0442\u0440\u0435\u0442\u044c\u0435\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block5_item4_text',
            field=models.CharField(default='\u041a\u0430\u0436\u0434\u044b\u0439 \u043c\u0430\u0433\u0430\u0437\u0438\u043d \u0441\u0442\u043e\u043b\u043a\u043d\u0435\u0442\u0441\u044f \u0441</br>\u043f\u0440\u043e\u0431\u043b\u0435\u043c\u043e\u0439 \u0447\u0435\u043b\u043e\u0432\u0435\u0447\u0435\u0441\u043a\u043e\u0433\u043e \u0444\u0430\u043a\u0442\u043e\u0440\u0430 \u0438</br>\u0432\u043e\u0440\u043e\u0432\u0441\u0442\u0432\u0430 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u0430', max_length=200, verbose_name='\u0411\u043b\u043e\u043a5 \u0422\u0435\u043a\u0441\u0442 \u0447\u0435\u0442\u0432\u0435\u0440\u043d\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block5_text',
            field=models.CharField(default='\u0421\u0422\u0410\u0422\u0418\u0421\u0422\u0418\u0427\u0415\u0421\u041a\u0418\u0415 \u0414\u0410\u041d\u041d\u042b\u0415', max_length=100, verbose_name='\u0411\u043b\u043e\u043a5 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block6_back',
            field=models.ImageField(default=b'images/decoration_2.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a6 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block6_text',
            field=models.CharField(default='\u041c\u042b \u0417\u0410\u0429\u0418\u0422\u0418\u041c \u0412\u0410\u0421 \u041e\u0422 \u042d\u0422\u0418\u0425 \u041f\u0420\u041e\u0411\u041b\u0415\u041c!', max_length=100, verbose_name='\u0411\u043b\u043e\u043a6 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block6_text2',
            field=models.CharField(default='* \u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0430 \u043d\u0435\u0437\u0430\u0432\u0438\u0441\u0438\u043c\u043e\u0439 \u044d\u043a\u0441\u043f\u0435\u0440\u0442\u043d\u043e\u0439 \u0433\u0440\u0443\u043f\u043f\u043e\u0439 "\u041f\u0440\u0435\u0434\u043f\u0440\u0438\u043d\u0438\u043c\u0430\u0442\u0435\u043b\u0438 \u042e\u0433\u0430">', max_length=200, verbose_name='\u0411\u043b\u043e\u043a6 \u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u043c', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block4_back_color',
            field=colorfield.fields.ColorField(default=b'#5287a7', max_length=10, verbose_name='\u0411\u043b\u043e\u043a4 \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block4_field_color',
            field=colorfield.fields.ColorField(default=b'#294353', max_length=10, verbose_name='\u0411\u043b\u043e\u043a4 \u0426\u0432\u0435\u0442 \u043f\u043e\u043b\u0435\u0439', blank=True),
        ),
    ]
