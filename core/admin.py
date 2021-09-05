from django.contrib import admin

from reversion.admin import VersionAdmin
from adminsortable2.admin import SortableAdminMixin

from core.models import Static, Category, Good, Project, Certificate, FAQItem, AboutUsInNumbers, Service

from seo import seo_fieldsets
from seo.forms import SEOForm


class StaticForm(SEOForm):
    class Meta:
        model = Static
        fields = []


@admin.register(Certificate)
class CertificateCompanyAdmin(VersionAdmin, admin.ModelAdmin):
    list_display = ['title', 'get_thumbnail', 'on_main']
    fields = ['title', 'cover', 'on_main']
    list_filter = ['title', 'on_main']


@admin.register(Static)
class StaticAdmin(VersionAdmin):
    list_display = ['title', 'slug', 'active']
    list_filter = ['active']
    list_editable = ['active']
    ordering = [ 'title', 'active']
    prepopulated_fields = {"slug": ["title"]}
    save_on_top = True
    save_as = True
    fieldsets = [
        (None, {'fields': ('title', 'content', 'active')}),
        (u'Мета информация для оптимизации', {'fields': ('slug', )})]
    fieldsets += seo_fieldsets


@admin.register(Category)
class CategoryAdmin(SortableAdminMixin, VersionAdmin):

    list_display = (
        'title', 'slug'
    )


@admin.register(Good)
class GoodAdmin(VersionAdmin):
    list_display = (
        'title', 'get_thumbnail', 'active', 'order'
    )

    list_editable = ('active', 'order')

    list_filter = ('active', 'category')


@admin.register(Service)
class ServiceAdmin(VersionAdmin):
    list_display = (
        'title', 'get_thumbnail', 'active', 'order'
    )

    list_editable = ('active', 'order')

    list_filter = ['active']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_cover_admin']
    readonly_fields = ['get_cover_admin']
    fieldsets = (
        ('Изображения', {
            'fields': ('title', 'description', 'get_cover_admin', 'date', 'folder'),
        }),
    )
    save_on_top = True
    save_as = True


@admin.register(FAQItem)
class FAQItemAdmin(SortableAdminMixin, VersionAdmin):

    list_display = (
        'question', 'answer', 'is_active'
    )

    list_editable = ('is_active',)

    list_filter = ('is_active', )


@admin.register(AboutUsInNumbers)
class AboutUsInNumbersAdmin(VersionAdmin):

    list_display = (
        'title', 'number', 'is_active'
    )

    list_editable = ('is_active',)

    list_filter = ('is_active', )
