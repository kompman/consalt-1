# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0015_auto_20150518_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='config',
            field=models.ForeignKey(default=1, to='config.SiteConfiguration'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block2_background',
            field=models.ImageField(default=b'images/hats.jpg', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a2 \u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430', blank=True),
        ),
    ]
