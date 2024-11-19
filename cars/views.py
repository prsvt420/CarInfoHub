from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.handlers.wsgi import WSGIRequest
from django.db.models import QuerySet
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from cars.forms import CarForm, CommentForm, CarUpdateForm
from cars.mixins import OwnerRequiredMixin
from cars.models import Car, Comment
from cars.permissions import IsOwnerOrReadOnly
from cars.serializers import CarSerializer, CommentSerializer
from cars.services import CommentService, CarService


class CarListView(ListView):
    model: Car = Car
    template_name: str = 'cars/cars-list.html'
    context_object_name: str = 'cars_list'
    paginate_by: int = 5


@method_decorator(login_required, name='post')
class CarDetailView(DetailView):
    model: Car = Car
    template_name: str = 'cars/cars-detail.html'
    context_object_name: str = 'car'

    def get_context_data(self, **kwargs: dict) -> dict:
        """Добавляет комментарии к контексту для отображения на странице деталей автомобиля."""

        context: dict = super().get_context_data(**kwargs)
        context['comments'] = CommentService.get_comments_for_car(self.object)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request: WSGIRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        """Добавляет комментарий к автомобилю."""

        car: Car = self.get_object()
        form: CommentForm = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = car
            comment.author = request.user
            comment.save()
            return redirect('cars:cars-detail', slug=car.slug)
        return self.get(request, *args, **kwargs)


class CarCreateView(LoginRequiredMixin, CreateView):
    model: Car = Car
    template_name: str = 'cars/cars-create.html'
    form_class: CarForm = CarForm
    success_url: str = reverse_lazy('cars:cars-list')

    def form_valid(self, form: CarForm) -> HttpResponse:
        """Валидирует форму и сохраняет автомобиль."""
        form.instance.owner = self.request.user
        return super().form_valid(form)


class CarUpdateView(OwnerRequiredMixin, UpdateView):
    model: Car = Car
    template_name: str = 'cars/cars-update.html'
    form_class: CarUpdateForm = CarUpdateForm

    def get_success_url(self) -> str:
        """Возвращает URL-адрес на который будет перенаправлен пользователь после обновления."""

        return reverse_lazy('cars:cars-detail', kwargs={'slug': self.object.slug})


class CarDeleteView(OwnerRequiredMixin, DeleteView):
    model: Car = Car
    success_url: str = reverse_lazy('cars:cars-list')


class CarViewSet(viewsets.ModelViewSet):
    queryset: QuerySet[Car] = CarService.get_all_cars()
    serializer_class: CarSerializer = CarSerializer
    permission_classes: tuple = (
        IsOwnerOrReadOnly,
    )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class: CommentSerializer = CommentSerializer
    permission_classes: tuple = (
        IsAuthenticatedOrReadOnly,
    )

    def get_queryset(self) -> QuerySet[Comment]:
        """Возвращает комментарии к автомобилю."""

        car_id: int = self.kwargs['car_id']
        comments = CommentService.get_comments_for_car_id(car_id)
        return comments

    def perform_create(self, serializer: CommentSerializer) -> None:
        """Добавляет комментарий к автомобилю."""

        car_id: int = self.kwargs['car_id']
        car: Car = CarService.get_car_by_id(car_id)
        serializer.save(car=car, author=self.request.user)
