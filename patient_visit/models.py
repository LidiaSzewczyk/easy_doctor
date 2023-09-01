from django.contrib.auth import get_user_model
from django.db import models

from patient.models import Patient
from visit.models import TimeStampedModel

user = get_user_model()


class PatientVisit(TimeStampedModel):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_visits', verbose_name='pacjent',
                               help_text='pacjent')
    doctor = models.ForeignKey(user, on_delete=models.CASCADE, related_name='patient_visits', verbose_name='lekarz',
                               help_text='lekarz', default=2)
    diagnosis = models.TextField(verbose_name='Rozpoznanie', null=True, blank=True)
    interview = models.TextField(verbose_name='Wywiad', null=True, blank=True)
    examination = models.TextField(verbose_name='Badanie', null=True, blank=True)
    recommendations = models.TextField(verbose_name='Zalecenia', null=True, blank=True)
    start_date = models.DateTimeField(verbose_name='Rozpoczęcie wizyty', null=True, blank=True)
    end_date = models.DateTimeField(verbose_name='Zakończenie wizyty', null=True, blank=True)
    is_deleted = models.BooleanField(default=False, verbose_name='Wizytz usunięta')

    def __str__(self):
        return self.patient.get_full_name()

    class Meta:
        verbose_name = 'wizyta'
        verbose_name_plural = 'wizyty'
