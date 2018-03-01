from django.shortcuts import render
from .models import Rejestracja
from .forms import RejestracjaForm
from django.views.generic import TemplateView, DetailView, CreateView
from .test import dni
from django.http import HttpResponse

class RejestracjaView(TemplateView):
    template_name = 'rejestracja/dietetycy.html'

class DietetykView(CreateView):
    #template_name = 'rejestracja/form.html'
    fields = '__all__'
    model = Rejestracja
    forms = RejestracjaForm


    def get_context_data(self, **kwargs):
        qs = Rejestracja.objects.all()
        gm = []
        for a in qs:
            gm.append(str(a).replace(':','').replace(' ',''))
        print(gm)
        context = super().get_context_data(**kwargs)
        context['forms'] = self.forms
        context['godziny'] = dni()
        context['dni'] = ('Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela')
        context['niedostepne'] = gm
        return context

    # def post(self, request, *args, **kwargs):
    #     form =RejestracjaForm(request.POST)
    #     context_new = {
    #         'object': 'OK',
    #        }
    #     if form.is_valid():
    #        print('ok')
    #
    #     return render(request,'rejestracja/rejestracja.html',context_new)


