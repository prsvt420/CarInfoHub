# Generated by Django 5.1.3 on 2024-11-18 13:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=128, verbose_name='Марка автомобиля')),
                ('model', models.CharField(max_length=128, verbose_name='Модель автомобиля')),
                ('year', models.IntegerField(verbose_name='Год выпуска')),
                ('description', models.TextField(verbose_name='Описание автомобиля')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания записи')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата и время последнего обновления записи')),
                ('slug', models.SlugField(max_length=128, unique=True, verbose_name='URL')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
                'db_table': 'cars',
                'db_table_comment': 'Таблица содержит данные об автомобилях',
                'ordering': ('make', 'model', 'year'),
            },
        ),
    ]
