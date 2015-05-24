# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0013_auto_20150504_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='block15_back',
            field=models.ImageField(default=b'images/footer.jpg', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a15 \u0424\u043e\u043d\u043e\u0432\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block15_button_color',
            field=colorfield.fields.ColorField(default=b'#fff600', max_length=10, verbose_name='\u0411\u043b\u043e\u043a15 \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block15_button_text',
            field=models.CharField(default='\u0417\u0410\u041a\u0410\u0417\u0410\u0422\u042c \u0417\u0412\u041e\u041d\u041e\u041a', max_length=100, verbose_name='\u0411\u043b\u043e\u043a15 \u0422\u0435\u043a\u0441\u0442 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block15_logo',
            field=models.ImageField(default=b'images/logo2.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a15 \u041b\u043e\u0433\u043e\u0442\u0438\u043f', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block15_phone',
            field=models.CharField(default='7 (918) 930-03-16', max_length=100, verbose_name='\u0411\u043b\u043e\u043a15 \u0422\u0435\u043b\u0435\u0444\u043e\u043d', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block15_text',
            field=models.CharField(default='<b>\u041c\u044b \u0441\u043e\u0437\u0434\u0430\u0435\u043c \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0438 \u043e\u0431\u0435\u0441\u043f\u0435\u0447\u0438\u0432\u0430\u044e\u0449\u0438\u0435 \u0412\u0430\u0448\u0435 \u0431\u0443\u0434\u0443\u0449\u0435\u0435!</b></br>\u0440\u0430\u0431\u043e\u0442\u0430\u0435\u043c \u0432 \u041a\u0440\u0430\u0441\u043d\u043e\u0434\u0430\u0440\u0441\u043a\u043e\u043c \u043a\u0440\u0430\u0435 \u0438 \u041a\u0440\u044b\u043c\u0443', max_length=200, verbose_name='\u0411\u043b\u043e\u043a15 \u0422\u0435\u043a\u0441\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block15_under_phone_text',
            field=models.CharField(default='email:info@consalt-bf.ru</br>\u0418\u041d\u041d 233603955530 \u041e\u0413\u0420\u041d 314231105100090', max_length=200, verbose_name='\u0411\u043b\u043e\u043a15 \u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u043e\u043c', blank=True),
        ),
        migrations.AlterField(
            model_name='siteconfiguration',
            name='block14_header',
            field=models.CharField(default='\u041d\u0410\u0428\u0418 \u041f\u0410\u0420\u0422\u041d\u0415\u0420\u042b', max_length=100, verbose_name='\u0411\u043b\u043e\u043a14 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
    ]
