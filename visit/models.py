from django.db import models
from django.urls import reverse


class TimeStampedModel(models.Model):
    """
    Model **TimeStampedModel** przechowuje daty stworzenia wpisu i aktualizacji wpisu do bazy danych.

    Zmienne:
        created_at: Data utworzenia wpisu
        updated_at: Data modyfikacji wpisu
    """

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Utworzono')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Zmodyfikowano')

    class Meta:
        abstract = True


class Diagnosis(TimeStampedModel):
    number = models.CharField(max_length=20, help_text='Numer', verbose_name='Numer')
    name = models.CharField(max_length=250, help_text='Nazwa', verbose_name='Nazwa')
    info = models.CharField(max_length=250, help_text='Dodatkowe info', verbose_name='Dodatkowe info', null=True,
                            blank=True, )
    slug = models.SlugField(max_length=250, null=True, unique=True)

    class Meta:
        verbose_name = 'Rozpoznanie'
        verbose_name_plural = 'Rozpoznania'

    def __str__(self):
        return self.number + ' - ' + self.name



