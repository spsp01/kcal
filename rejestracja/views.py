from django.shortcuts import render
from .models import Rejestracja
from .forms import RejestracjaForm
from django.views.generic import TemplateView, DetailView, CreateView
from .test import dni
from django.http import HttpResponse
from django.http import JsonResponse


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

    def post(self, request, *args, **kwargs):
         form = RejestracjaForm(request.POST)

         context_new = {
             'object': 'OK',
            }
         if form.is_valid():
            imie = form.cleaned_data['imię']
            email = form.cleaned_data['email']
            dietetyk = form.cleaned_data['dietetyk']
            dzień = form.cleaned_data['dzień']
            godzina = form.cleaned_data['godzina']
            obj, created = Rejestracja.objects.get_or_create(imię=imie,email=email,dietetyk=dietetyk,dzień=dzień,godzina=godzina)
            if created:
                obj.save()
                return JsonResponse(context_new)
            else:
                context_new = {
                    'object': 'Nie można zarejestrować - podana data i godzina jest już zarezerwowana',
                }
         return JsonResponse(context_new)


def detail(request, *args, **kwargs):
    if request.method == "POST":
        imie = request.POST.get('imię')
        email = request.POST.get('email')
        dietetyk = request.POST.get('dietetyk')
        dzień = request.POST.get('dzień')
        godzina = request.POST.get('godzina')

        print(imie)
        print(email)
        print(dietetyk)
        print(dzień)
        print(godzina)

        #Prosta Walidacja długości imienia
        if len(imie) > 3:
            print(imie)
            Rejestracja(imię=imie,email=email,dietetyk=dietetyk,dzień=dzień,godzina=godzina)
            Rejestracja.save(self)


        #Walidacja maila
        email = request.POST.get('email')
        #test = Rejestracja.objects.all()

        return HttpResponse({'imię':imie,'email':email})
    return render(request, 'rejestracja/rejestracja_formc.html', {'poll': 'p'})