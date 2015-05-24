# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='block1_background',
            field=colorfield.fields.ColorField(max_length=10, verbose_name='\u0411\u043b\u043e\u043a1 \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block1_button_color',
            field=colorfield.fields.ColorField(max_length=10, verbose_name='\u0411\u043b\u043e\u043a1 \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block1_button_text',
            field=models.CharField(max_length=100, verbose_name='\u0411\u043b\u043e\u043a1 \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block1_logo',
            field=models.ImageField(upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a1 \u041b\u043e\u0433\u043e\u0442\u0438\u043f', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block1_phone',
            field=models.CharField(max_length=100, verbose_name='\u0411\u043b\u043e\u043a1 \u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block1_text',
            field=models.CharField(max_length=200, verbose_name='\u0411\u043b\u043e\u043a1 \u0422\u0435\u043a\u0441\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='blocks',
            field=multiselectfield.db.fields.MultiSelectField(default=b'1,2', max_length=35, verbose_name='\u0411\u043b\u043e\u043a\u0438', choices=[(1, '\u0411\u043b\u043e\u043a1'), (2, '\u0411\u043b\u043e\u043a2'), (3, '\u0411\u043b\u043e\u043a3'), (4, '\u0411\u043b\u043e\u043a4'), (5, '\u0411\u043b\u043e\u043a5'), (6, '\u0411\u043b\u043e\u043a6'), (7, '\u0411\u043b\u043e\u043a7'), (8, '\u0411\u043b\u043e\u043a8'), (9, '\u0411\u043b\u043e\u043a9'), (10, '\u0411\u043b\u043e\u043a10'), (11, '\u0411\u043b\u043e\u043a11'), (12, '\u0411\u043b\u043e\u043a12'), (13, '\u0411\u043b\u043e\u043a13'), (14, '\u0411\u043b\u043e\u043a14'), (15, '\u0411\u043b\u043e\u043a15')]),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='site_name',
            field=models.CharField(default='\u041a\u043e\u043d\u0441\u0443\u043b\u044c\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0438 \u043f\u0440\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u0430\u044f \u043f\u043e\u043c\u043e\u0449\u044c \u043f\u043e \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u044e \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u043e\u0432', max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u0430\u0439\u0442\u0430'),
        ),
    ]
