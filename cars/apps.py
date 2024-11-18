from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'cars'
    verbose_name: str = 'Автомобили'
