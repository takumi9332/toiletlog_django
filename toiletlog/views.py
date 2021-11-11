from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from toiletlog.models import Toilet
from .forms import ToiletForm


class Index(ListView):
    model = Toilet


class Detail(DetailView):
    model = Toilet


class Create(CreateView):
    model = Toilet
    form_class = ToiletForm


class Update(UpdateView):
    template_name = 'toiletlog/toilet_update_form.html'
    model = Toilet
    form_class = ToiletForm


class Delete(DeleteView):
    model = Toilet
    success_url = "/"
