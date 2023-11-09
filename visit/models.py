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

    def get_absolute_url(self):
        return reverse('visit:diagnosis_detail', kwargs={'slug': self.slug})


class Part(models.Model):
    name = models.CharField(max_length=250, help_text='Nazwa', verbose_name='Nazwa')

    class Meta:
        verbose_name = 'Część'
        verbose_name_plural = 'Część'

    def __str__(self):
        return self.name


class Priority(models.Model):
    part = models.ForeignKey('Part', related_name='priorities', on_delete=models.CASCADE, help_text='Część',
                             verbose_name='Część')
    priority = models.IntegerField(help_text='Kolejność', verbose_name='Kolejność')
    text = models.ForeignKey('Text', related_name='priorities', on_delete=models.CASCADE, help_text='Tekst',
                             verbose_name='Tekst')
    diagnosis = models.ForeignKey('Diagnosis', help_text='Rozpoznanie', verbose_name='Rozpoznanie',
                                  on_delete=models.CASCADE, related_name='priorities')

    class Meta:
        verbose_name = 'Przypisanie'
        verbose_name_plural = 'Przypisanie'

    def __str__(self):
        return self.part.name + str(self.priority)


class Text(TimeStampedModel):
    title = models.CharField(max_length=200, help_text='Tytuł', verbose_name='Tytuł')
    doctor_text = models.TextField(help_text='Dla lekarza', verbose_name='Dla lekarza', null=True, blank=True)
    patient_text = models.TextField(help_text='Dla pacjenta', verbose_name='Dla pacjenta', null=True, blank=True, )
    slug = models.SlugField(max_length=250, null=True, unique=True)
    form_type = models.ForeignKey('FormType', related_name='choices', on_delete=models.CASCADE, help_text='formularz',
                                  verbose_name='formularz', null=True, blank=True)

    class Meta:
        verbose_name = 'Tekst'
        verbose_name_plural = 'Teksty'

    def __str__(self):
        return self.doctor_text


class FormType(models.Model):
    name = models.CharField(max_length=150, help_text='nazwa', verbose_name='nazwa')
    info = models.CharField(max_length=150, help_text='info', verbose_name='info', null=True, blank=True)

    class Meta:
        verbose_name = 'Typ formularza'
        verbose_name_plural = 'Typy formularza'

    def __str__(self):
        return self.info or self.name


class Choice(models.Model):
    text = models.ForeignKey('Text', related_name='choices', on_delete=models.CASCADE, help_text='Text',
                             verbose_name='Text')
    doctor_choice = models.TextField(max_length=500, help_text='Dla lekarza', verbose_name='Dla lekarza')
    patient_choice = models.TextField(max_length=500, help_text='Dla pacjenta', verbose_name='Dla pacjenta')
    priority = models.IntegerField(help_text='Kolejność', verbose_name='Kolejność')

    class Meta:
        verbose_name = 'Wybór'
        verbose_name_plural = 'Wybory'

    def __str__(self):
        return self.doctor_choice + ' - ' + self.patient_choice
