from django.db import connection
from django.views.generic import ListView, DetailView

from visit.models import Diagnosis


class DiagnosisListView(ListView):
    queryset = Diagnosis.objects.all()
    context_object_name = 'diagnosis'
    template_name = 'visit/diagnosis_list.html'
    # paginate_by = 10


class DiagnosisDetailView(DetailView):
    model = Diagnosis
    template_name = 'visit/diagnosis_detail.html'
    context_object_name = 'diagnosis'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        diagnosis = self.object
        all_texts = diagnosis.priorities.all()
        print(connection.queries)

        context["contents"] = {
            'Wywiad': [(x.text.doctor_text, x.text.patient_text,
                        [(el.doctor_choice, el.patient_choice, el.priority) for el in
                         x.text.choices.all().order_by('priority')], 'w' + str(x.priority), x.text.form_type,
                        [el.patient_choice for el in x.text.choices.all()]) for x in
                       all_texts.filter(part__name='Wywiad').order_by('priority')],
            'Badanie': [(x.text.doctor_text, x.text.patient_text,
                         [(el.doctor_choice, el.patient_choice, el.priority) for el in
                          x.text.choices.all().order_by('priority')], 'b' + str(x.priority), x.text.form_type,
                         [el.patient_choice for el in x.text.choices.all()]) for x in
                        all_texts.filter(part__name='Badanie fizykalne').order_by('priority')],
            # 'Rozpoznanie': diagnosis.number + '   ' + diagnosis.name,
            'Zalecenia': [(x.text.doctor_text, x.text.patient_text,
                           [(el.doctor_choice, el.patient_choice, el.priority) for el in
                            x.text.choices.all().order_by('priority')], 'z' + str(x.priority), x.text.form_type,
                           [el.patient_choice for el in x.text.choices.all()]) for x
                          in all_texts.filter(part__name='Zalecenia').order_by('priority')],

        }
        print(10 * "*", type(context), "context", context)
        return context
