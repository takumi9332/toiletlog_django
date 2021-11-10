from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from .forms import LoginForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import activate_user

from .forms import SignUpForm


class Top(generic.TemplateView):
    template_name = 'toiletlog/toilet_list.html'


class Login(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


class Logout(LogoutView):
    template_name = 'toiletlog/toilet_list.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('users:login')
    template_name = 'registration/signup.html'


class ActivateView(TemplateView):
    template_name = "registration/activate.html"

    def get(self, request, uidb64, token, *args, **kwargs):
        result = activate_user(uidb64, token)
        return super().get(request, result=result, **kwargs)
