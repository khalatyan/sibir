# Generated by Django 2.2 on 2021-09-05 07:59

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('core', '0004_goodscategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512, verbose_name='Заголовок')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Описание')),
                ('active', models.BooleanField(default=True, verbose_name='Активный')),
                ('price_hour', models.CharField(blank=True, max_length=64, null=True, verbose_name='Цена товара за час')),
                ('price_change', models.CharField(blank=True, max_length=64, null=True, verbose_name='Цена товара за смену')),
                ('order', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Порядок')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Category', verbose_name='категория')),
                ('good_image', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.FILER_IMAGE_MODEL, verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['order'],
            },
        ),
    ]
