from django import forms
from django.forms import fields, widgets
from .models import Prefecture, Toilet


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
