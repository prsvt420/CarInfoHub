from datetime import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from cars.utils.text import generate_slug


class Car(models.Model):
    make: str = models.CharField(max_length=128, verbose_name='Марка автомобиля')
    model: str = models.CharField(max_length=128, verbose_name='Модель автомобиля')
    year: int = models.IntegerField(verbose_name='Год выпуска')
    description: str = models.TextField(verbose_name='Описание автомобиля')
    created_at: datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания записи'
    )
    updated_at: datetime = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время последнего обновления записи'
    )
    owner: User = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')
    slug: str = models.SlugField(max_length=128, verbose_name='URL', unique=True)

    class Meta:
        db_table: str = 'cars'
        db_table_comment: str = 'Таблица содержит данные об автомобилях'
        verbose_name: str = 'Автомобиль'
        verbose_name_plural: str = 'Автомобили'
        ordering: tuple = ('make', 'model', 'year')

    def __str__(self) -> str:
        return f'{self.make} {self.model}'

    def save(
            self,
            *args,
            force_insert=False,
            force_update=False,
            using=None,
            update_fields=None,
    ) -> None:
        self.slug = generate_slug(self.make, self.model, self.year)
        super().save(*args, force_insert, force_update, using, update_fields)

    def get_absolute_url(self) -> str:
        """Возвращает URL-адрес страницы для просмотра конкретного автомобиля."""
        return reverse('cars:cars-detail', kwargs={'slug': self.slug})


class Comment(models.Model):
    content: str = models.TextField(verbose_name='Содержание комментария')
    created_at: datetime = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания комментария'
    )
    car: Car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    author: User = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        db_table: str = 'comments'
        db_table_comment: str = 'Таблица содержит комментарии к автомобилям'
        verbose_name: str = 'Комментарий'
        verbose_name_plural: str = 'Комментарии'
        ordering: tuple = ('created_at',)

    def __str__(self) -> str:
        return self.content
