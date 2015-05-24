# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0007_auto_20150501_0751'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='block7_back',
            field=models.ImageField(default=b'images/rezult.jpg', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a7 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0444\u043e\u043d\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block7_item1_icon',
            field=models.ImageField(default=b'images/rez_1.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a7 \u041f\u0443\u043d\u043a\u04421 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block7_item1_text',
            field=models.CharField(default='\u0410\u0434\u0435\u043a\u0432\u0430\u0442\u043d\u0430\u044f \u0438</br>\u043b\u0438\u0431\u0435\u0440\u0430\u043b\u044c\u043d\u0430\u044f</br>\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043d\u0430 \u0443\u0441\u043b\u0443\u0433\u0438</br></br>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a7 \u0422\u0435\u043a\u0441\u0442 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block7_item2_icon',
            field=models.ImageField(default=b'images/rez_2.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a7 \u041f\u0443\u043d\u043a\u04422 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block7_item2_text',
            field=models.CharField(default='\u0420\u0430\u0431\u043e\u0442\u0430\u0435\u043c \u0442\u043e\u043b\u044c\u043a\u043e</br>\u0432 \u043f\u0440\u0430\u043a\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u043c \u043f\u043e\u043b\u0435</br></br></br>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a7 \u0422\u0435\u043a\u0441\u0442 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block7_item3_icon',
            field=models.ImageField(default=b'images/rez_3.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a7 \u041f\u0443\u043d\u043a\u04423 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block7_item3_text',
            field=models.CharField(default='\u042d\u043a\u0441\u043f\u0435\u0440\u0442\u044b \u0438\u0437</br>\u043f\u0440\u043e\u0444\u0435\u0441\u0441\u0438\u043e\u043d\u0430\u043b\u044c\u043d\u043e\u0439</br>\u044d\u043b\u0438\u0442\u044b \u0431\u0438\u0437\u043d\u0435\u0441\u0430</br></br>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a7 \u0422\u0435\u043a\u0441\u0442 \u0442\u0440\u0435\u0442\u044c\u0435\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block7_item4_icon',
            field=models.ImageField(default=b'images/rez_4.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a7 \u041f\u0443\u043d\u043a\u04424 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block7_item4_text',
            field=models.CharField(default='\u0418\u043d\u043e\u0441\u0442\u0440\u0430\u043d\u043d\u044b\u0435</br>\u044d\u043a\u0441\u043f\u0435\u0440\u0442\u044b \u0432 \u043e\u0431\u043b\u0430\u0441\u0442\u0438</br>\u0430\u0440\u0445\u0438\u0442\u0435\u043a\u0442\u0443\u0440\u044b \u0438</br>\u043f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u0430', max_length=200, verbose_name='\u0411\u043b\u043e\u043a7 \u0422\u0435\u043a\u0441\u0442 \u0447\u0435\u0442\u0432\u0435\u0440\u043d\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block7_item5_icon',
            field=models.ImageField(default=b'images/rez_5.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a7 \u041f\u0443\u043d\u043a\u04425 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block7_item5_text',
            field=models.CharField(default='\u041e\u043f\u0435\u0440\u0430\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c</br>\u043f\u0440\u0438\u043d\u044f\u0442\u0438\u044f \u0440\u0435\u0448\u0435\u043d\u0438\u0439 \u0441</br>\u043d\u0430\u0446\u0435\u043b\u0435\u043d\u043d\u043e\u0441\u0442\u044c\u044e \u043d\u0430</br>\u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442', max_length=200, verbose_name='\u0411\u043b\u043e\u043a7 \u0422\u0435\u043a\u0441\u0442 \u0447\u0435\u0442\u0432\u0435\u0440\u043d\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block7_text',
            field=models.CharField(default='\u041f\u041e\u0427\u0415\u041c\u0423 \u041c\u042b \u0413\u0410\u0420\u0410\u041d\u0422\u0418\u0420\u0423\u0415\u041c \u0420\u0415\u0417\u0423\u041b\u042c\u0422\u0410\u0422', max_length=100, verbose_name='\u0411\u043b\u043e\u043a7 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_back',
            field=models.ImageField(default=b'images/bg_1.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a8 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0444\u043e\u043d\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_button_color',
            field=colorfield.fields.ColorField(default=b'#fff600', max_length=10, verbose_name='\u0411\u043b\u043e\u043a8 \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_button_text',
            field=models.CharField(default='\u041d\u0410\u0427\u0410\u0422\u042c \u0421\u041e\u0422\u0420\u0423\u0414\u041d\u0418\u0427\u0415\u0421\u0422\u0412\u041e', max_length=100, verbose_name='\u0411\u043b\u043e\u043a8 \u0422\u0435\u043a\u0441\u0442 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_item1_icon',
            field=models.ImageField(default=b'images/client_1.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a8 \u041f\u0443\u043d\u043a\u04421 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_item1_text',
            field=models.CharField(default='\u0411\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u044b\u0439</br>\u0431\u0438\u0437\u043d\u0435\u0441</br></br>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a8 \u0422\u0435\u043a\u0441\u0442 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_item2_icon',
            field=models.ImageField(default=b'images/client_2.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a8 \u041f\u0443\u043d\u043a\u04422 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_item2_text',
            field=models.CharField(default='\u0413\u0440\u0430\u043c\u043e\u0442\u043d\u044b\u0439 \u0438</br>\u043e\u0431\u0443\u0447\u0435\u043d\u043d\u044b\u0439</br>\u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b', max_length=200, verbose_name='\u0411\u043b\u043e\u043a8 \u0422\u0435\u043a\u0441\u0442 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_item3_icon',
            field=models.ImageField(default=b'images/client_3.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a8 \u041f\u0443\u043d\u043a\u04423 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_item3_text',
            field=models.CharField(default='\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043d</br>-\u043d\u044b\u0435 \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u044b</br>\u0440\u0430\u0431\u043e\u0442\u044b', max_length=200, verbose_name='\u0411\u043b\u043e\u043a8 \u0422\u0435\u043a\u0441\u0442 \u0442\u0440\u0435\u0442\u044c\u0435\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_item4_icon',
            field=models.ImageField(default=b'images/client_4.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a8 \u041f\u0443\u043d\u043a\u04424 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_item4_text',
            field=models.CharField(default='\u0421\u0435\u0440\u0432\u0438\u0441\u043d\u043e\u0435</br>\u0441\u043e\u043f\u0440\u043e\u0432\u043e\u0436\u0434\u0435\u043d\u0438\u0435</br></br>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a8 \u0422\u0435\u043a\u0441\u0442 \u0447\u0435\u0442\u0432\u0435\u0440\u043d\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_item5_icon',
            field=models.ImageField(default=b'images/client_5.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a8 \u041f\u0443\u043d\u043a\u04425 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_item5_text',
            field=models.CharField(default='\u0421\u0442\u0430\u0431\u0438\u043b\u044c\u043d\u044b\u0439</br>\u0434\u043e\u0445\u043e\u0434</br></br>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a8 \u0422\u0435\u043a\u0441\u0442 \u0447\u0435\u0442\u0432\u0435\u0440\u043d\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block8_text',
            field=models.CharField(default='\u0421\u041e\u0422\u0420\u0423\u0414\u041d\u0418\u0427\u0410\u042f \u0421 \u041d\u0410\u041c\u0418</br><span>\u041d\u0410\u0428\u0418 \u041a\u041b\u0418\u0415\u041d\u0422\u042b \u041f\u041e\u041b\u0423\u0427\u0410\u042e\u0422</span>', max_length=100, verbose_name='\u0411\u043b\u043e\u043a8 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
    ]
