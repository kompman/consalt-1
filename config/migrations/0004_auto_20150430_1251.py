# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0003_auto_20150430_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block1_text',
            field=models.CharField(default='\u041f\u043e\u043c\u043e\u0449\u044c \u043f\u0440\u0438 \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u0438 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u043e\u0432</br>\u0441 \u0433\u0430\u0440\u0430\u043d\u0442\u0438\u0435\u0439 \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u043f\u0440\u0438\u0431\u044b\u043b\u0438</br><span>\u0432 \u041a\u0440\u0430\u0441\u043d\u043e\u0434\u0430\u0440\u0441\u043a\u043e\u043c \u043a\u0440\u0430\u0435 \u0438 \u041a\u0440\u044b\u043c\u0443</span>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a1 \u0422\u0435\u043a\u0441\u0442', blank=True),
        ),
    ]
