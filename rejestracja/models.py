from django.db import models
from django.urls import reverse

class Rejestracja(models.Model):
    DIETETYK = (('1', 'Jan Kowalski'), ('2', 'Ada Wspaniała'))
    imię = models.CharField(max_length=255)
    email = models.EmailField()
    dietetyk = models.CharField(max_length=255, choices=DIETETYK, default='1')
    dzień = models.DateField()
    godzina = models.DateTimeField()

    # def get_absolute_url(self):
    #      return reverse('rejestracja-detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.imię