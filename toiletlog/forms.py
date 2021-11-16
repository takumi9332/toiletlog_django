from django import forms
from django.forms import fields, widgets
from .models import Comment, Prefecture, Toilet


class ToiletForm(forms.ModelForm):

    class Meta:
        model = Toilet
        fields = ['title', 'prefecture', 'city', 'address', 'building',
                  'sex', 'type', 'washlet', 'cleanliness', 'info', 'image']
        widgets = {
            'sex': forms.RadioSelect(),
            'type': forms.RadioSelect(),
            'washlet': forms.RadioSelect(),
            'cleanliness': forms.RadioSelect(),
        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('target', 'created_at')
