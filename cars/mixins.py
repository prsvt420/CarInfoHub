from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseForbidden, HttpResponse
from django.views import View

from cars.models import Car


class OwnerRequiredMixin(View):
    def dispatch(self, request: WSGIRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        car_object: Car = self.get_object()

        if car_object.owner != request.user:
            return HttpResponseForbidden('У вас нет прав для выполнения этого действия.')
        return super().dispatch(request, *args, **kwargs)
