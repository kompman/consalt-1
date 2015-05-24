# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0014_auto_20150504_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='siteconfiguration',
            name='blocks',
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block11_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block12_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block13_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block14_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block15_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block1_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block2_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block3_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block4_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block5_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block6_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block7_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_visibility',
            field=models.BooleanField(default=True, verbose_name='\u041f\u043e\u043a\u0430\u0437\u044b\u0432\u0430\u0442\u044c'),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block14_header',
            field=models.CharField(default='\u041d\u0410\u0428\u0418 \u041f\u0410\u0420\u0422\u041d\u0415\u0420\u042b', help_text='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u043e\u0432 \u0434\u043e\u0431\u0430\u0432\u043b\u044f\u044e\u0442\u0441\u044f \u0447\u0435\u0440\u0435\u0437 \u043c\u0435\u043d\u044e "\u041f\u0430\u0440\u0442\u043d\u0435\u0440\u044b"', max_length=100, verbose_name='\u0411\u043b\u043e\u043a14 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block9_header',
            field=models.CharField(default='\u041d\u0410\u0428\u0418 \u0423\u0421\u041b\u0423\u0413\u0418', max_length=100, verbose_name='\u0411\u043b\u043e\u043a9 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
    ]
