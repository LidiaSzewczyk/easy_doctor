from django.views.generic import ListView, DetailView

from patient.models import Patient


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

        context["content"] = {
            'Dane': '',
            'Wizyty': '',

        }
        print(10 * "*", type(context), "context", context)
        return context
