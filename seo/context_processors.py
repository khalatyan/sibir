# -*- coding: utf-8 -*-
from seo.models import ExSEO


def ex_seo(request):
    try:
        seo = ExSEO.objects.get(url=request.META["PATH_INFO"])
    except Exception:
        seo = None
    return {
        "ex_meta_keywords": seo.meta_keywords if seo else None,
        "ex_meta_description": seo.meta_description if seo else None,
        "ex_html_title": seo.html_title if seo else None,
    }
