from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from toiletlog.models import Comment, Toilet
from .forms import CommentCreateForm, ToiletForm
from django.shortcuts import get_object_or_404, redirect, render


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


class CommentCreate(generic.CreateView):
    template_name = 'comment_form.html'
    model = Comment
    form_class = CommentCreateForm

    def form_valid(self, form):
        toilet_pk = self.kwargs['pk']
        toilet = get_object_or_404(Toilet, pk=toilet_pk)
        comment = form.save(commit=False)
        comment.target = toilet
        comment.save()
        return redirect('detail', pk=toilet_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['toilet'] = get_object_or_404(Toilet, pk=self.kwargs['pk'])
        return context
