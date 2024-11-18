from django.contrib import admin

from cars.models import Car, Comment


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    fields: tuple = (
        'make',
        'model',
        'year',
        'description',
        'owner',
        'slug',
        'created_at',
        'updated_at',
    )
    list_display: tuple = ('car_name', 'year', 'created_at', 'owner')
    search_fields: tuple = ('make', 'model', 'year', 'description', 'owner')
    list_filter: tuple = ('make', 'model', 'year', 'owner')
    readonly_fields: tuple = ('created_at', 'updated_at', 'slug')
    date_hierarchy: str = 'created_at'

    @admin.display(description='Автомобиль')
    def car_name(self, obj: Car) -> str:
        """
        Возвращает название автомобиля состоящее из марки и модели

        Params:
            obj: Car
                Объект автомобиля

        Returns:
            str: Название автомобиля
        """
        return str(obj)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display: tuple = ('car', 'content', 'created_at', 'author')
    search_fields: tuple = ('car', 'content', 'author')
    list_filter: tuple = ('car', 'author')
    date_hierarchy: str = 'created_at'
