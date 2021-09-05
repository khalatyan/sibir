# -*- coding: utf-8 -*-
from django.contrib import admin

from seo.models import ExSEO
from seo.forms import SEOForm


class ExSEOForm(SEOForm):
    class Meta(object):
        model = ExSEO
        fields = []


class ExSEOAdmin(admin.ModelAdmin):
    form = ExSEOForm

    list_display = ('name', 'url',)
    list_per_page = 30

    fieldsets = (
        (u'Основные', {
            'classes': ('wide',),
            'fields': ('name', 'url',)
        }),
        (u'SEO', {
            'classes': ('wide',),
            'fields': ('html_title', 'meta_description', 'meta_keywords')
        })
    )


admin.site.register(ExSEO, ExSEOAdmin)