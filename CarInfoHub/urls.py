from typing import List

from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from CarInfoHub import settings

urlpatterns: List[path] = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('users/', include('users.urls', namespace='users'), name='users'),
    path('cars/', include('cars.urls', namespace='cars'), name='cars'),
]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
