from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include

from core import views as core_views

urlpatterns = [
    path('admin-sibir/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('send_message_ajax/', core_views.send_message_ajax),

    path('', core_views.IndexView.as_view(), name='index_view'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'core.views.handle_404_view'
handler500 = 'core.views.handle_500_view'
