# Generated by Django 2.2 on 2021-09-05 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_certificate_faqitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUsInNumbers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Цифра')),
                ('title', models.TextField(verbose_name='Заголовок')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'О нас в цифрах',
                'verbose_name_plural': 'О нас в цифрах',
            },
        ),
    ]
