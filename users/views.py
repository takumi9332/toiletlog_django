from django.contrib.auth.views import LoginView, LogoutView
from django.views import generic
from .forms import LoginForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

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
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
