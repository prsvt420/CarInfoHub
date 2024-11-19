from typing import List

from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from .yasg import urlpatterns as yasg_urls

from CarInfoHub import settings
from cars.views import CarViewSet, CommentViewSet

api_router: DefaultRouter = DefaultRouter()
api_router.register(r'cars', CarViewSet, basename='car')

urlpatterns: List[path] = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
    path('users/', include('users.urls', namespace='users'), name='users'),
    path('cars/', include('cars.urls', namespace='cars'), name='cars'),
    path('api/', include(api_router.urls), name='api'),
    path('api/cars/<int:car_id>/comments/', CommentViewSet.as_view(
        {
            'get': 'list',
            'post': 'create',
        }), name='car-comments'),
    path('api/auth/', include(arg='djoser.urls'), name='auth'),
    path('api/auth/', include(arg='djoser.urls.authtoken'), name='auth-token'),
]

urlpatterns += yasg_urls

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
