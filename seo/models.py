# -*- coding: utf-8 -*-
from django.db import models

class SEO(models.Model):
    """
    Абстрактная модель для создания и управления моделями с SEO.
    """
    html_title = models.CharField(u"HTML Title", max_length=128, default=u"", blank=True)

    # META данные
    meta_description = models.CharField("description", max_length=255, blank=True)
    meta_keywords = models.CharField("keywords", max_length=255, blank=True)

    seo_text = models.TextField(u"SEO текст", blank=True)

    class Meta:
        abstract = True

    def get_html_title(self):
        if self.html_title:
            return self.html_title
        return u""

    def get_seo_context(self):
        return {
            "html_title": self.html_title,
            "meta_description": self.meta_description,
            "meta_keywords": self. meta_keywords,
            "seo_text": self.seo_text
        }


class ExSEO(SEO):
    """
    Управление SEO данными отдельной страницы.
    """
    name = models.CharField(u"Название", max_length=255, blank=True)
    url = models.CharField(u"URL", max_length=255)

    class Meta:
        verbose_name = u"SEO"
        verbose_name_plural = u"SEO"