from django import forms
from django.forms import ModelForm
from .models import Rejestracja

class RejestracjaForm(ModelForm):
   #imię = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Wpisz swoje imię'}),)
    class Meta:
        model = Rejestracja
        fields = '__all__'
        widgets = {
          'imię': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Wpisz swoje imię'}),
          'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Wpis email'}),
          'dietetyk': forms.Select(attrs={'class': 'form-control'}),
          'dzień': forms.Select(attrs={'class': 'form-control'}),

        }
