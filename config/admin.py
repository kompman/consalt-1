#! coding: utf-8
from django import forms
from django.db import models
from django.contrib import admin
from django.contrib.admin.widgets import AdminFileWidget
from django.utils.safestring import mark_safe
from django.forms import ModelForm

from solo.admin import SingletonModelAdmin
from sorl.thumbnail import get_thumbnail
from redactor.widgets import RedactorEditor


from config.models import SiteConfiguration, Partner


class AIW(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            t = get_thumbnail(value, '300x150')
            output.append('<img src="{}">'.format(t.url))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class PartnerInline(admin.TabularInline):
    model = Partner
    formfield_overrides = {
        models.ImageField: {'widget': AIW},
    }


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(SingletonModelAdmin):
    inlines = [PartnerInline]
    formfield_overrides = {
        models.CharField: {'widget': RedactorEditor()},
        models.ImageField: {'widget': AIW},
        models.TextField: {'widget': RedactorEditor()},
    }

    fieldsets = (
        (None, {
            'fields': ('site_name', )
        }),
        (u'Блок1', {
            'classes': ('grp-collapse grp-open',),
            'fields': ('block1_visibility', 'block1_background', 'block1_logo', 'block1_text', 'block1_phone', 'block1_button_color',
                       'block1_button_text')
        }),
        (u'Блок2', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('block2_visibility', 'block2_background', 'block2_text')
        }),
        (u'Блок3', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('block3_visibility', 'block3_text', 'block3_image', 'block3_list_icon', 'block3_item1', 'block3_item1_text',
                       'block3_item2', 'block3_item2_text', 'block3_item3', 'block3_item3_text', 'block3_time')
        }),
        (u'Блок4', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('block4_visibility', 'block4_text', 'block4_button_text', 'block4_under_button_text', 'block4_back_color',
                       'block4_button_color', 'block4_field_color')
        }),
        (u'Блок5', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('block5_visibility', 'block5_text', 'block5_back', 'block5_item1_text', 'block5_item2_text', 'block5_item3_text',
                       'block5_item4_text')
        }),
        (u'Блок6', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('block6_visibility', 'block6_text', 'block6_back', 'block6_text2')
        }),
        (u'Блок7', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('block7_visibility', 'block7_text', 'block7_back', 'block7_item1_icon', 'block7_item1_text', 'block7_item2_icon',
                       'block7_item2_text', 'block7_item3_icon', 'block7_item3_text', 'block7_item4_icon',
                       'block7_item4_text', 'block7_item5_icon', 'block7_item5_text')
        }),
        (u'Блок8', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('block8_visibility', 'block8_text', 'block8_back', 'block8_item1_icon', 'block8_item1_text', 'block8_item2_icon',
                       'block8_item2_text', 'block8_item3_icon', 'block8_item3_text', 'block8_item4_icon',
                       'block8_item4_text', 'block8_item5_icon', 'block8_item5_text', 'block8_button_color',
                       'block8_button_text')
        }),
        (u'Блок9', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('block9_visibility', 'block9_header', 'block9_under_text', 'block9_item_color', 'block9_item1_text',
                       'block9_item2_text', 'block9_item3_text', 'block9_item4_text', 'block9_item5_text',
                       'block9_item6_text', 'block9_item7_text', 'block9_item8_text', 'block9_item9_text',
                       'block9_button_color', 'block9_button_text')
        }),
        (u'Блок10', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('block10_visibility', 'block10_background', 'block10_text', 'block10_image', 'block10_list_icon', 'block10_item1',
                       'block10_item1_text', 'block10_item2', 'block10_item2_text', 'block10_item3',
                       'block10_item3_text', 'block10_time', 'block10_text1', 'block10_button_text',
                       'block10_under_button_text', 'block10_back_color', 'block10_button_color', 'block10_field_color')
        }),
        (u'Блок11', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('block11_visibility', 'block11_text', 'block11_back_color', 'block11_square_color', 'block11_number_color',
                       'block11_item1_number', 'block11_item1_text', 'block11_item2_number', 'block11_item2_text',
                       'block11_item3_number', 'block11_item3_text', 'block11_item4_number', 'block11_item4_text',
                       'block11_item5_number', 'block11_item5_text')
        }),
        (u'Блок12', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('block12_visibility', 'block12_text', 'block12_back', 'block12_image', 'block12_item1_text', 'block12_item2_text',
                       'block12_item3_text', 'block12_item4_text', 'block12_item5_text', 'block12_button_text',
                       'block12_button_color')
        }),
        (u'Блок13', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('block13_visibility', 'block13_header', 'block13_image1', 'block13_fio1', 'block13_event1', 'block13_text1',
                       'block13_image2', 'block13_fio2', 'block13_event2', 'block13_text2')
        }),
        (u'Блок14', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('block14_visibility', 'block14_header',)
        }),
        (u'Блок15', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('block15_visibility', 'block15_logo', 'block15_back', 'block15_text', 'block15_button_color', 'block15_button_text',
            'block15_phone', 'block15_under_phone_text')
        }),
    )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    pass