from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.core.mail import send_mail

from visit.models import TimeStampedModel

user = get_user_model()


class Patient(TimeStampedModel):
    first_name = models.CharField(max_length=150, verbose_name='imię', help_text='imię')
    last_name = models.CharField(max_length=150, verbose_name='nazwisko', help_text='nazwisko')
    email = models.EmailField(verbose_name='email', help_text='email')
    birth_date = models.DateField(verbose_name='Data urodzenia', help_text='Data urodzenia')
    address = models.CharField(max_length=250, verbose_name='adres', help_text='adres')
    pesel = models.CharField(max_length=20, verbose_name='PESEL', help_text='PESEL')
    phone = models.CharField(max_length=15, verbose_name='Tel.', help_text='Tel.', null=True, blank=True)
    doctor = models.ForeignKey(user, on_delete=models.CASCADE, related_name='patients', verbose_name='lekarz',
                               help_text='lekarz')

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    # def email_user(self, subject, message, from_email=None, **kwargs):
    #     """Send an email to this user."""
    #     send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        verbose_name = 'pacjent'
        verbose_name_plural = 'pacjenci'

    def __str__(self):
        return self.get_full_name()
