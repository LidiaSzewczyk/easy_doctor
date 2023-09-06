from datetime import date

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from patient.helpers import calc_age
from .forms import PatientVisitForm, PatientVisitUpdateForm
from .models import PatientVisit


class PatientVisitCreateView(CreateView):
    template_name = 'visit/base_visit.html'
    form_class = PatientVisitForm
    model = PatientVisit


class PatientVisitListView(ListView):
    queryset = PatientVisit.objects.all()
    context_object_name = 'patient_visits'
    template_name = 'patient_visit/patient_visit_list.html'

    # paginate_by = 10

    def post(self, request, *args, **kwargs):
        return PatientVisitCreateView.as_view()(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient_visit_form'] = PatientVisitForm()
        return context


class PatientVisitDetailView(DetailView):
    model = PatientVisit
    template_name = 'patient_visit/patientvisit_detail.html'
    context_object_name = 'visit'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["age_now"] = calc_age(self.object.patient.birth_date, date.today())
        context["age_visit"] = calc_age(self.object.patient.birth_date, self.object.start_date.date())
        patient = self.object.patient
        filter_criteria = {'patient': patient}
        all_patient_visits = PatientVisit.objects.filter(**filter_criteria).values('pk', 'start_date', 'diagnosis')
        context["all_patient_visits"] = all_patient_visits
        context['patient'] = patient
        context['patient_visit_form'] = PatientVisitForm()
        return context

    def post(self, request, *args, **kwargs):
        return PatientVisitCreateView.as_view()(request)


class PatientVisitUpdateView(UpdateView):
    model = PatientVisit
    template_name = 'patient_visit/patientvisit_update.html'
    context_object_name = 'visit'
    form_class = PatientVisitUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["age_now"] = calc_age(self.object.patient.birth_date, date.today())
        context["age_visit"] = calc_age(self.object.patient.birth_date, self.object.start_date.date())
        filter_criteria = {'patient': self.object.patient}
        all_patient_visits = PatientVisit.objects.filter(**filter_criteria).values('pk', 'start_date', 'diagnosis')
        context["all_patient_visits"] = all_patient_visits
        context['patient_visit_form'] = PatientVisitForm()
        return context

    def post(self, request, *args, **kwargs):

        if 'patient_visit_submit' in request.POST:
            return PatientVisitCreateView.as_view()(request)

        if 'patient_visit_update_submit' in request.POST:
            return super().post(request, *args, **kwargs)


class PatientVisitDeleteView(DeleteView):
    model = PatientVisit
    context_object_name = 'patient_visit'

    def get_success_url(self):
        patient = PatientVisit.objects.get(pk=self.kwargs['pk']).patient.pk
        success_url = reverse_lazy('patient:patient_detail', args=[patient])
        return success_url.format(**self.object.__dict__)
