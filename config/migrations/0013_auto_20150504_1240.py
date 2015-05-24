# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0012_auto_20150504_1233'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435', blank=True)),
                ('image', models.ImageField(upload_to=b'images/', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u041f\u0430\u0440\u0442\u043d\u0435\u0440',
                'verbose_name_plural': '\u041f\u0430\u0440\u0442\u043d\u0435\u0440\u044b',
            },
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block14_header',
            field=models.CharField(default='\u041e\u0422\u0417\u042b\u0412\u042b \u041d\u0410\u0428\u0418\u0425 \u041a\u041b\u0418\u0415\u041d\u0422\u041e\u0412', max_length=100, verbose_name='\u0411\u043b\u043e\u043a13 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
    ]
