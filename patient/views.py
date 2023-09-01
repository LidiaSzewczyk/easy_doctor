from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from datetime import date

from patient_visit.models import PatientVisit
from .forms import PatientForm
from .helpers import calc_age
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["age"] = calc_age(self.object.birth_date, date.today())
        filter_criteria = {'patient': self.object}
        all_patient_visits = PatientVisit.objects.filter(**filter_criteria).values('pk','start_date', 'diagnosis')
        context["all_patient_visits"] = all_patient_visits
        return context


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
