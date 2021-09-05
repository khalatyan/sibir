# -*- coding: utf-8 -*-

from django import forms

class SEOForm(forms.ModelForm):
    html_title = forms.CharField(label=u"HTML заголовок",widget=forms.TextInput(attrs={'style':'width:760px'}), required=False, max_length=128)
    meta_keywords = forms.CharField(label=u"Ключевые слова", max_length=255, widget=forms.TextInput(attrs={'style':'width:760px'}), required=False)
    meta_description = forms.CharField(max_length=255, label=u"Описание", widget=forms.Textarea(attrs={'cols':'80','rows':'4'}), required=False)
    seo_text = forms.CharField(label=u"SEO Текст", widget=forms.Textarea(attrs={'cols':'80','rows':'8'}), required=False)

