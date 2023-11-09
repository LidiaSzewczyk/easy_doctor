from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from datetime import date

from patient_visit.forms import PatientVisitForm
from patient_visit.models import PatientVisit
from patient_visit.views import PatientVisitCreateView
from .forms import PatientForm
from .helpers import calc_age
from .models import Patient


class PatientListView(LoginRequiredMixin, ListView):
    queryset = Patient.objects.all()
    context_object_name = 'patients'
    template_name = 'patient/patients_list.html'

    def post(self, request, *args, **kwargs):
        return PatientVisitCreateView.as_view()(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient_visit_form'] = PatientVisitForm()
        return context


class PatientDetailView(LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'patient/patient_detail.html'
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["age"] = calc_age(self.object.birth_date, date.today())
        filter_criteria = {'patient': self.object}
        all_patient_visits = PatientVisit.objects.filter(**filter_criteria).values('pk', 'start_date', 'diagnosis')
        context["all_patient_visits"] = all_patient_visits
        context['patient_visit_form'] = PatientVisitForm()
        return context

    def post(self, request, *args, **kwargs):
        return PatientVisitCreateView.as_view()(request)


class PatientCreateView(LoginRequiredMixin, CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient_visit_form'] = PatientVisitForm()
        return context

    def post(self, request, *args, **kwargs):
        if 'patient_visit_submit' in request.POST:
            return PatientVisitCreateView.as_view()(request)

        if 'patient_create_submit' in request.POST:
            return super().post(request, *args, **kwargs)


class PatientUpdateView(LoginRequiredMixin, UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient_create.html'
    context_object_name = 'patient'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient_visit_form'] = PatientVisitForm()
        return context

    def post(self, request, *args, **kwargs):
        if 'patient_visit_submit' in request.POST:
            return PatientVisitCreateView.as_view()(request)

        if 'patient_create_submit' in request.POST:
            return super().post(request, *args, **kwargs)


class PatientDeleteView(LoginRequiredMixin, DeleteView):
    model = Patient
    success_url = reverse_lazy('patient:patient_list')
    context_object_name = 'patient'
