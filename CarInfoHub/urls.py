from typing import List

from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include

from CarInfoHub import settings

urlpatterns: List[path] = [
    path('admin/', admin.site.urls),
    path('cars/', include('cars.urls', namespace='cars'), name='cars'),
]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
