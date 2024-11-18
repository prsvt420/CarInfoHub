from typing import List

from django.urls import path

from cars import views

app_name: str = 'cars'

urlpatterns: List[path] = [
    path('', views.CarListView.as_view(), name='cars-list'),
    path('create/', views.CarCreateView.as_view(), name='cars-create'),
    path('update/<slug:slug>/', views.CarUpdateView.as_view(), name='cars-update'),
    path('delete/<slug:slug>/', views.CarDeleteView.as_view(), name='cars-delete'),
    path('<slug:slug>/', views.CarDetailView.as_view(), name='cars-detail'),
]
