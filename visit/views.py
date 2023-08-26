from django.views.generic import ListView

from visit.models import Diagnosis


class DiagnosisListView(ListView):
    queryset = Diagnosis.objects.all()
    context_object_name = 'diagnosis'
    template_name = 'visit/diagnosis_list.html'
    # paginate_by = 10
