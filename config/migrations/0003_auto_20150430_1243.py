# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0002_auto_20150430_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block1_logo',
            field=models.ImageField(default=b'logo.png', upload_to=b'images/', verbose_name='\u0411\u043b\u043e\u043a1 \u041b\u043e\u0433\u043e\u0442\u0438\u043f'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='blocks',
            field=multiselectfield.db.fields.MultiSelectField(default=b'1,2,3,4,5,6,7,8,9,10,11,12,13,14,15', max_length=35, verbose_name='\u0411\u043b\u043e\u043a\u0438', choices=[(1, '\u0411\u043b\u043e\u043a1'), (2, '\u0411\u043b\u043e\u043a2'), (3, '\u0411\u043b\u043e\u043a3'), (4, '\u0411\u043b\u043e\u043a4'), (5, '\u0411\u043b\u043e\u043a5'), (6, '\u0411\u043b\u043e\u043a6'), (7, '\u0411\u043b\u043e\u043a7'), (8, '\u0411\u043b\u043e\u043a8'), (9, '\u0411\u043b\u043e\u043a9'), (10, '\u0411\u043b\u043e\u043a10'), (11, '\u0411\u043b\u043e\u043a11'), (12, '\u0411\u043b\u043e\u043a12'), (13, '\u0411\u043b\u043e\u043a13'), (14, '\u0411\u043b\u043e\u043a14'), (15, '\u0411\u043b\u043e\u043a15')]),
        ),
    ]
