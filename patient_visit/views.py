from datetime import date

from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, FormView

from patient.helpers import calc_age
from .forms import PatientVisitForm
from .models import PatientVisit


class PatientVisitFormView(FormView):
    template_name = 'visit/base_visit.html'
    form_class = PatientVisitForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient_visit_form'] = PatientVisitForm()

        return context


class PatientVisitListView(ListView, PatientVisitFormView):
    queryset = PatientVisit.objects.all()
    context_object_name = 'patient_visits'
    template_name = 'patient_visit/patient_visit_list.html'
    # paginate_by = 10


class PatientVisitDetailView(DetailView, PatientVisitFormView):
    model = PatientVisit
    template_name = 'patient_visit/patientvisit_detail.html'
    context_object_name = 'visit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["age_now"] = calc_age(self.object.patient.birth_date, date.today())
        context["age_visit"] = calc_age(self.object.patient.birth_date, self.object.start_date.date())
        filter_criteria = {'patient': self.object.patient}
        all_patient_visits = PatientVisit.objects.filter(**filter_criteria).values('pk', 'start_date', 'diagnosis')
        context["all_patient_visits"] = all_patient_visits
        return context
