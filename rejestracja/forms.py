from django import forms
from django.core.validators import MinLengthValidator
from django.forms import ModelForm
from .models import Rejestracja

class RejestracjaForm(ModelForm):
    class Meta:
        model = Rejestracja
        fields = '__all__'
        widgets = {
          'imię': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Wpisz swoje imię'}),
          'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Wpis email'}),
          'dietetyk': forms.HiddenInput(),
          'dzień': forms.HiddenInput(),
          'godzina': forms.HiddenInput(),
        }

