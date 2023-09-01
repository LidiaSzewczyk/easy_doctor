from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from .models import PatientVisit


class PatientVisitListView(ListView):
    queryset = PatientVisit.objects.all()
    context_object_name = 'patient_visits'
    template_name = 'patient_visit/patient_visit_list.html'
    # paginate_by = 10

    # def get_absolute_url(self):
    #     return reverse('patient_visit:patient_visit_list', kwargs={'pk': self.pk})
