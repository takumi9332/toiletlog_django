from django.views.generic import ListView, DetailView

from toiletlog.models import Toilet


class Index(ListView):
    model = Toilet


class Detail(DetailView):
    model = Toilet
