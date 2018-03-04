from django.db import models
from django.urls import reverse
from django.core.validators import validate_email
from .utils import godziny

class Rejestracja(models.Model):
    DIETETYK = (('1', 'Jan Kowalski'), ('2', 'Ada Wspaniała'))
    DZIEN = (('1','Poniedziałek'),('2','Wtorek'), ('3','Środa'), ('4','Czwartek'),('5','Piątek'), ('6','Sobota'), ('7','Niedziela'))
    imię = models.CharField(max_length=255)
    email = models.EmailField()
    dietetyk = models.CharField(max_length=255, choices=DIETETYK, default='1')
    dzień = models.CharField(max_length=255,choices=DZIEN)
    godzina = models.CharField(max_length=255,)

    def get_absolute_url(self):
        return self.dietetyk

    def __str__(self):
        return self.godzina+' '+str(self.dzień)


