from django.db import models

class Rejestracja(models.Model):
    imię = models.CharField()
    email = models.EmailField()
    dietetyk = models.CharField()
    dzień = models.DateField()
    godzina = models.DateTimeField()


