# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0008_auto_20150501_0821'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_back_color',
            field=colorfield.fields.ColorField(default=b'#5287a7', max_length=10, verbose_name='\u0411\u043b\u043e\u043a4 \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_button_color',
            field=colorfield.fields.ColorField(default=b'#fff600', max_length=10, verbose_name='\u0411\u043b\u043e\u043a4 \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_button_text',
            field=models.CharField(default='\u041f\u041e\u041b\u0423\u0427\u0418\u0422\u042c \u0411\u0415\u0421\u041f\u041b\u0410\u0422\u041d\u041e', max_length=100, verbose_name='\u0411\u043b\u043e\u043a4 \u0422\u0435\u043a\u0441\u0442 \u043d\u0430 \u043a\u043d\u043e\u043f\u043a\u0435', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_field_color',
            field=colorfield.fields.ColorField(default=b'#294353', max_length=10, verbose_name='\u0411\u043b\u043e\u043a4 \u0426\u0432\u0435\u0442 \u043f\u043e\u043b\u0435\u0439', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_image',
            field=models.ImageField(default=b'images/decoration_1.jpg', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a3 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043f\u043e\u0434 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u043c', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_item1',
            field=models.BooleanField(default=True, verbose_name='\u0411\u043b\u043e\u043a3 \u041f\u0435\u0440\u0432\u044b\u0439 \u043f\u0443\u043d\u043a\u0442'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_item1_text',
            field=models.CharField(default='\u041f\u043e\u0448\u0430\u0433\u043e\u0432\u044b\u0439 \u043f\u043b\u0430\u043d \u043e\u0442\u043a\u0440\u044b\u0442\u0438\u044f \u043c\u0438\u043d\u0438\u043c\u0430\u0440\u043a\u0435\u0442\u0430', max_length=200, verbose_name='\u0411\u043b\u043e\u043a3 \u0422\u0435\u043a\u0441\u0442 \u043f\u0435\u0440\u0432\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_item2',
            field=models.BooleanField(default=True, verbose_name='\u0411\u043b\u043e\u043a3 \u0412\u0442\u043e\u0440\u043e\u0439 \u043f\u0443\u043d\u043a\u0442'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_item2_text',
            field=models.CharField(default='\u041c\u0435\u0442\u043e\u0434 \u0443\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u044f \u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0447\u0435\u043a\u0430 \u0432 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0435', max_length=200, verbose_name='\u0411\u043b\u043e\u043a3 \u0422\u0435\u043a\u0441\u0442 \u0432\u0442\u043e\u0440\u043e\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_item3',
            field=models.BooleanField(default=True, verbose_name='\u0411\u043b\u043e\u043a3 \u0422\u0440\u0435\u0442\u0438\u0439 \u043f\u0443\u043d\u043a\u0442'),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_item3_text',
            field=models.CharField(default='3D \u043c\u043e\u0434\u0435\u043b\u044c \u0432\u0430\u0448\u0435\u0433\u043e \u0431\u0443\u0434\u0443\u0449\u0435\u0433\u043e \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430', max_length=200, verbose_name='\u0411\u043b\u043e\u043a3 \u0422\u0435\u043a\u0441\u0442 \u0442\u0440\u0435\u0442\u044c\u0435\u0433\u043e \u043f\u0443\u043d\u043a\u0442\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_list_icon',
            field=models.ImageField(default=b'images/ok.png', upload_to=b'images/', null=True, verbose_name='\u0411\u043b\u043e\u043a3 \u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0434\u043b\u044f \u0441\u043f\u0438\u0441\u043a\u0430', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_text',
            field=models.CharField(default='\u0422\u041e\u041b\u042c\u041a\u041e \u0421\u0415\u0413\u041e\u0414\u041d\u042f!</br>\u0412\u044b \u043f\u043e\u043b\u0443\u0447\u0430\u0435\u0442\u0435<span> \u0411\u0415\u0421\u041f\u041b\u0410\u0422\u041d\u041e!</span>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a3 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_text1',
            field=models.CharField(default='\u0423\u0427\u0410\u0421\u0422\u0412\u0423\u0419\u0422\u0415 \u0412 \u0410\u041a\u0426\u0418\u0418</br><span>\u0438 \u0412\u0430\u0448 \u0431\u0438\u0437\u043d\u0435\u0441 \u0432\u044b\u0439\u0434\u0435\u0442</br>\u043d\u0430 \u043d\u043e\u0432\u044b\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c!</span>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a4 \u0422\u0435\u043a\u0441\u0442', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_time',
            field=models.TimeField(default=b'08:31:57', null=True, verbose_name='\u0412\u0440\u0435\u043c\u044f \u0434\u043e \u043a\u043e\u043d\u0446\u0430 \u0430\u043a\u0446\u0438\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block10_under_button_text',
            field=models.CharField(default='\u0412\u0430\u0448\u0438 \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0435 \u0434\u0430\u043d\u043d\u044b\u0435 \u0432 \u0431\u0435\u0437\u043e\u043f\u0430\u0441\u043d\u043e\u0441\u0442\u0438</br>\u0438 \u043d\u0435 \u0431\u0443\u0434\u0443\u0442 \u043f\u0435\u0440\u0435\u0434\u0430\u043d\u044b \u0442\u0440\u0435\u0442\u044c\u0438\u043c \u043b\u0438\u0446\u0430\u043c', max_length=100, verbose_name='\u0411\u043b\u043e\u043a4 \u0422\u0435\u043a\u0441\u0442 \u043f\u043e\u0441\u043b\u0435 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_button_color',
            field=colorfield.fields.ColorField(default=b'#fff600', max_length=10, verbose_name='\u0411\u043b\u043e\u043a9 \u0426\u0432\u0435\u0442 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_button_text',
            field=models.CharField(default='\u041f\u041e\u041b\u0423\u0427\u0418\u0422\u042c \u0411\u0415\u0421\u041f\u041b\u0410\u0422\u041d\u0423\u042e \u041a\u041e\u041d\u0421\u0423\u041b\u042c\u0422\u0410\u0426\u0418\u042e', max_length=100, verbose_name='\u0411\u043b\u043e\u043a8 \u0422\u0435\u043a\u0441\u0442 \u043a\u043d\u043e\u043f\u043a\u0438', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_header',
            field=models.CharField(default='\u041d\u0410\u0428\u0418 \u0423\u0421\u041b\u0423\u0413\u0418>', max_length=100, verbose_name='\u0411\u043b\u043e\u043a9 \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_item1_text',
            field=models.CharField(default='<span>\u0417\u0430\u043c\u0435\u0440 \u044d\u043a\u043e\u043d\u043e\u043c\u0438\u0447\u0435\u0441\u043a\u043e\u0439</span>&nbsp; \u044d\u0444\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u0438</br>\u043c\u0435\u0441\u0442\u043e\u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0442\u043e\u0440\u0433\u043e\u0432\u043e\u0439 \u0442\u043e\u0447\u043a\u0438', max_length=200, verbose_name='\u0411\u043b\u043e\u043a9 \u0422\u0435\u043a\u0441\u04421', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_item2_text',
            field=models.CharField(default='<span>\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u043a\u043e\u043d\u0446\u0435\u043f\u0446\u0438\u0438 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430:</span>&nbsp; \u043f\u043e</br>\u0446\u0435\u043d\u0435, \u043f\u043e \u0442\u043e\u0432\u0430\u0440\u0443, \u043f\u043e \u0441\u0435\u0440\u0432\u0438\u0441\u0443 \u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f', max_length=200, verbose_name='\u0411\u043b\u043e\u043a9 \u0422\u0435\u043a\u0441\u04422', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_item3_text',
            field=models.CharField(default='<span>\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0441\u0445\u0435\u043c\u044b</span>&nbsp; \u044d\u0444\u0444\u0435\u043a\u0442\u0438\u0432\u043d\u043e\u0433\u043e</br>\u0440\u0430\u0441\u043f\u043e\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u0442\u043e\u0440\u0433\u043e\u0432\u043e\u0433\u043e \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u044f -</br>\u043f\u0440\u0430\u0432\u0438\u043b\u043e \u043f\u043e\u0442\u043e\u043a\u0430 \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u0435\u0439</br>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a9 \u0422\u0435\u043a\u0441\u04423', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_item4_text',
            field=models.CharField(default='<span>\u041f\u0440\u043e\u0435\u043a\u0442 \u0430\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0437\u0430\u0446\u0438\u0438</span>&nbsp; \u043f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0432</br>\u0440\u0430\u0431\u043e\u0442\u044b \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430: \u041f\u041e, \u043a\u0430\u0441\u0441\u043e\u0432\u044b\u0439 \u043f\u043e\u0441\u0442, IP</br>\u043a\u043e\u043d\u0442\u0440\u043e\u043b\u044c \u0442\u043e\u0432\u0430\u0440\u0430, \u043f\u0440\u0438\u0435\u043c\u043a\u0430 \u0438 \u043e\u0442\u043f\u0443\u0441\u043a</br>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a9 \u0422\u0435\u043a\u0441\u04424', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_item5_text',
            field=models.CharField(default='<span>\u0412\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u044b</span>&nbsp; \u0432\u044b\u043a\u043b\u0430\u0434\u043a\u0438 \u0442\u043e\u0432\u0430\u0440\u043e\u0432 \u043d\u0430</br>\u043f\u043e\u043b\u043a\u0435 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430 - \u043f\u0440\u0430\u0432\u0438\u043b\u043e \u0437\u043e\u043b\u043e\u0442\u043e\u0439 \u043f\u043e\u043b\u043a\u0438 \u0438</br>\u0445\u043e\u0434\u043e\u0432\u043e\u0439 \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u0438', max_length=200, verbose_name='\u0411\u043b\u043e\u043a9 \u0422\u0435\u043a\u0441\u04425', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_item6_text',
            field=models.CharField(default='<span>\u0412\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u0435 \u0441\u0438\u0441\u0442\u0435\u043c\u044b</span>&nbsp; \u043c\u043e\u0442\u0438\u0432\u0430\u0446\u0438\u0438 \u0438</br>\u043e\u0442\u0432\u0435\u0442\u0441\u0442\u0432\u0435\u043d\u043d\u043e\u0441\u0442\u0438 \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u0430 (\u043e\u0431\u0443\u0447\u0435\u043d\u0438\u0435</br>\u043f\u0435\u0440\u0441\u043e\u043d\u0430\u043b\u0430 \u0441 \u043d\u043e\u043b\u044f)', max_length=200, verbose_name='\u0411\u043b\u043e\u043a9 \u0422\u0435\u043a\u0441\u04426', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_item7_text',
            field=models.CharField(default='<span>\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430 \u0438 \u0432\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u0435</span>&nbsp; \u043c\u0430\u0440\u043a\u0435\u0442\u0438\u043d\u0433\u043e\u0432\u044b\u0445</br>"\u044f\u043a\u043e\u0440\u0435\u0439" \u0434\u043b\u044f \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u0430 (\u0443\u0432\u0435\u043b\u0438\u0447\u0435\u043d\u0438\u0435</br>\u0441\u0440\u0435\u0434\u043d\u0435\u0433\u043e \u0447\u0435\u043a\u0430)', max_length=200, verbose_name='\u0411\u043b\u043e\u043a9 \u0422\u0435\u043a\u0441\u04427', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_item8_text',
            field=models.CharField(default='<span>\u0412\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b</span>&nbsp;\u0430\u043d\u0430\u043b\u0438\u0437\u0430</br>\u043e\u0431\u043e\u0440\u0430\u0447\u0438\u0432\u0430\u0435\u043c\u043e\u0441\u0442\u0438 \u043f\u043e\u043b\u043e\u0447\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0441\u0442\u0440\u0430\u043d\u0441\u0442\u0432\u0430</br></br>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a9 \u0422\u0435\u043a\u0441\u04428', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_item9_text',
            field=models.CharField(default='<span>\u041e\u0431\u0443\u0447\u0435\u043d\u0438\u0435 \u0441\u043e\u0431\u0441\u0442\u0432\u0435\u043d\u043d\u0438\u043a\u043e\u0432 \u0431\u0438\u0437\u043d\u0435\u0441\u0430</span>&nbsp;(\u0432\u044b\u0445\u043e\u0434</br>\u043d\u0430 \u0441\u0435\u0442\u0435\u0432\u043e\u0439 \u0444\u043e\u0440\u043c\u0430\u0442)</br>', max_length=200, verbose_name='\u0411\u043b\u043e\u043a9 \u0422\u0435\u043a\u0441\u04429', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_item_color',
            field=colorfield.fields.ColorField(default=b'#5287a7', max_length=10, verbose_name='\u0411\u043b\u043e\u043a9 \u0426\u0432\u0435\u0442 \u0444\u043e\u043d\u0430 \u0446\u0438\u0444\u0440', blank=True),
        ),
        migrations.AddField(
            model_name='siteconfiguration',
            name='block9_under_text',
            field=models.CharField(default='\u041e\u0442\u043a\u0440\u044b\u0442\u0438\u0435 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u043e\u0432 \u0441\u0430\u043c\u043e\u043e\u0431\u0441\u043b\u0443\u0436\u0438\u0432\u0430\u043d\u0438\u044f:</br>\u043e\u0442 \u0432\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0433\u043e \u043f\u0440\u043e\u0435\u043a\u0442\u0430 \u0434\u043e \u0433\u0430\u0440\u0430\u043d\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u043e\u0433\u043e \u043f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u044f \u043f\u0440\u0438\u0431\u044b\u043b\u0438', max_length=200, verbose_name='\u0411\u043b\u043e\u043a9 \u0442\u0435\u043a\u0441\u0442 \u043f\u043e\u0434 \u0437\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u043e\u043c', blank=True),
        ),
    ]
