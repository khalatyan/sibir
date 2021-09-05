# Generated by Django 2.2 on 2021-09-05 07:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('core', '0005_good'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveSmallIntegerField(verbose_name='Порядок')),
                ('question', models.CharField(max_length=256, verbose_name='Вопрос')),
                ('answer', models.TextField(verbose_name='Ответ')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'вопрос и ответ',
                'verbose_name_plural': 'Вопросы и ответы',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Наименование')),
                ('on_main', models.BooleanField(default=True, verbose_name='Отображать на главной')),
                ('cover', filer.fields.image.FilerImageField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.FILER_IMAGE_MODEL, verbose_name='сертификат')),
            ],
            options={
                'verbose_name': 'сертификат',
                'verbose_name_plural': 'Сертификаты',
                'ordering': ['title'],
            },
        ),
    ]