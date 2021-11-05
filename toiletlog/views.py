from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from toiletlog.models import Toilet


class Index(ListView):
    model = Toilet


class Detail(DetailView):
    model = Toilet


class Create(CreateView):
    model = Toilet

    fields = ["title", "prefecture", "city", "address", "building",
              "sex", "type", "washlet", "clean", "info", "image"]


class Update(UpdateView):
    model = Toilet

    fields = ["title", "prefecture", "city", "address", "building",
              "sex", "type", "washlet", "clean", "info", "image"]


class Delete(DeleteView):
    model = Toilet

    success_url = "/"
