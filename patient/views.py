from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PatientForm
from .models import Patient


class PatientListView(ListView):
    queryset = Patient.objects.all()
    context_object_name = 'patients'
    template_name = 'patient/patients_list.html'
    # paginate_by = 10


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patient/patient_detail.html'
    context_object_name = 'patient'


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient_create.html'


class PatientUpdateView(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patient/patient_create.html'
    context_object_name = 'patient'


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('patient:patient_list')
