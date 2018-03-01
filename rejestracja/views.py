from django.shortcuts import render
from .models import Rejestracja
from .forms import RejestracjaForm
from django.views.generic import TemplateView, DetailView, CreateView
from .test import dni

class RejestracjaView(TemplateView):
    template_name = 'rejestracja/dietetycy.html'

class DietetykView(CreateView):
    #template_name = 'rejestracja/form.html'
    fields = '__all__'
    model = Rejestracja
    forms = RejestracjaForm

    # def get_form(self):
    #     form = super(UserCreate, self).get_form(form_class)
    #     return form

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['forms'] = self.forms
        context['godziny'] = dni()
        context['dni'] = ('Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela')
        return context
