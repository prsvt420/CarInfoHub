from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views import View
from django.views.generic import CreateView


class UserLoginView(LoginView):
    form_class: AuthenticationForm = AuthenticationForm
    template_name: str = 'users/login.html'
    redirect_authenticated_user: str = True


class UserRegistrationView(CreateView):
    form_class: UserCreationForm = UserCreationForm
    template_name: str = 'users/registration.html'


class UserLogoutView(View):
    @staticmethod
    def get(request: WSGIRequest) -> HttpResponse:
        logout(request)
        return redirect('/')
