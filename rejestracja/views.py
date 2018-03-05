from django.shortcuts import render
from .models import Rejestracja
from .forms import RejestracjaForm
from django.views.generic import TemplateView, DetailView, CreateView
from .utils import godziny, is_alpha
from django.http import HttpResponse, JsonResponse, HttpRequest, HttpResponseRedirect
from django.urls import resolve, reverse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail

class RejestracjaView(TemplateView):
    template_name = 'rejestracja/dietetycy.html'

class DietetykView(CreateView):
    fields = '__all__'
    model = Rejestracja
    forms = RejestracjaForm

    def get_context_data(self, **kwargs):
        awqs = Rejestracja.objects.filter(dietetyk=2)
        jkqs = Rejestracja.objects.filter(dietetyk=1)
        aw = []
        for a in awqs:
            aw.append(str(a).replace(':','').replace(' ',''))
        jk = []
        for a in jkqs:
            jk.append(str(a).replace(':', '').replace(' ', ''))

        context = super().get_context_data(**kwargs)
        context['forms'] = self.forms
        context['godziny'] = godziny()
        context['dni'] = ('Poniedziałek', 'Wtorek', 'Środa', 'Czwartek', 'Piątek', 'Sobota', 'Niedziela')
        context['niedostepne_jk'] = jk
        context['niedostepne_aw'] = aw
        context['dietetyk']= ()
        return context

    def post(self, request, *args, **kwargs):
         form = RejestracjaForm(request.POST)
         blad = 1
         text_resp = 'Błąd w formularzu'
         context_new = {
             'object': text_resp,
             'blad': blad
         }
         if form.is_valid():
            imie = form.cleaned_data['imię']
            email = form.cleaned_data['email']
            dietetyk = form.cleaned_data['dietetyk']
            dzień = form.cleaned_data['dzień']
            godzina = form.cleaned_data['godzina']
            if len(imie) < 3:
              text_resp = 'Błąd - imię nie posiada 2 znaków'
              context_new = {
                  'object': text_resp,
                  'blad': blad
              }
              return JsonResponse(context_new)
            if not is_alpha(imie):
              text_resp = 'Błąd - imię nie może zawierać cyfr i znaków specjalnych'
              context_new = {
                  'object': text_resp,
                  'blad': blad
              }
              return JsonResponse(context_new)

            try:
              validate_email(email)
            except:
              context_new = {
                    'object': text_resp,
                    'blad': blad
                }
              text_resp = 'Niepoprawny email'
              return JsonResponse(context_new)

            obj, created = Rejestracja.objects.get_or_create(imię=imie,email=email,dietetyk=dietetyk,dzień=dzień,godzina=godzina)
            if created:
                text_resp = '/success?imie='+imie+'&dietetyk='+dietetyk+'&dzien='+dzień+'&godzina='+godzina
                blad = 0
                context_new = {
                    'object': text_resp,
                    'blad': blad,
                }
                obj.save()
                try:
                    send_mail(
                   'Potwierdzenie rejestracji', 'Witaj zarejestrowałeś się do dietetyka na godzinę '+ str(godzina), 'dietetyk@dietetyk.com', [str(email)], fail_silently=False,
                    )
                except:
                    print('Nieprawidłowo skonfigurowany serwer poczty')
                return JsonResponse(context_new)
            else:
                text_resp ='Nie można zarejestrować - podana data i godzina jest już zarezerwowana'
                context_new = {
                    'object': text_resp,
                    'blad': blad
                }
                return JsonResponse(context_new)
         return JsonResponse(context_new)

@csrf_exempt
def success(request):
    if request.method == "GET":
         try:
             if request.GET.get('godzina'):
                godzina = request.GET.get('godzina')
             if request.GET.get('imie'):
                imie = request.GET.get('imie')
             if request.GET.get('dietetyk'):
                dietetyk = request.GET.get('dietetyk')
             if request.GET.get('dzien'):
                dzien = request.GET.get('dzien')
             ditetyk_odm = ['Jana Kowalskiego', 'Ady Wspaniałej']
             dni = ['najbliższy poniedziałek', 'najbliższy wtorek', ' najbliższą środę', 'najbliższy czwartek',
                    'najbliższy piątek', 'najbliższą sobotę', 'najbliższą niedzielę']
             ditetyk_odm_list = int(dietetyk) - 1
             dzien_list = int(dzien) - 1
             text_resp = 'Witaj ' + str(imie) + '! Zarejestrowałeś się do dietetyka ' + ditetyk_odm[
                 ditetyk_odm_list] + ' w ' + dni[dzien_list] + ' o godznie ' + godzina
             if int(dietetyk) == 2:
                 img = 'doctor-female.png'
             else:
                 img = 'doctor-male.jpg'
             my_dict = {'text_resp': text_resp,
                        'img':img
                       }
             return render(request, 'rejestracja/success.html', my_dict)
         except:
             return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')