from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from patient.helpers import calc_age
from .forms import PatientVisitForm, PatientVisitUpdateForm
from .models import PatientVisit


class PatientVisitCreateView(LoginRequiredMixin, CreateView):
	template_name = 'visit/base_visit.html'
	form_class = PatientVisitForm
	model = PatientVisit


class PatientVisitListView(LoginRequiredMixin, ListView):
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


class PatientVisitDetailView(LoginRequiredMixin, DetailView):
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


class PatientVisitUpdateView(LoginRequiredMixin, UpdateView):
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


class PatientVisitDeleteView(LoginRequiredMixin, DeleteView):
	model = PatientVisit
	context_object_name = 'patient_visit'
	
	def get_success_url(self):
		patient = PatientVisit.objects.get(pk=self.kwargs['pk']).patient.pk
		success_url = reverse_lazy('patient:patient_detail', args=[patient])
		return success_url.format(**self.object.__dict__)


import io
from django.http import FileResponse, HttpResponse
from reportlab.pdfgen import canvas


def some_view(request, pk):
	# Create a file-like buffer to receive PDF data.
	buffer = io.BytesIO()
	
	# Create the PDF object, using the buffer as its "file."
	p = canvas.Canvas(buffer)
	
	# Draw things on the PDF. Here's where the PDF generation happens.
	# See the ReportLab documentation for the full list of functionality.
	p.drawString(100, 100, f"Hello world.  {str(pk)}")
	
	# Close the PDF object cleanly, and we're done.
	p.showPage()
	p.save()
	
	# FileResponse sets the Content-Disposition header so that browsers
	# present the option to save the file.
	buffer.seek(0)
	pdf_content = FileResponse(buffer, as_attachment=True, filename="hello.pdf")
	# Create an HttpResponse with PDF content type
	response = HttpResponse(pdf_content, content_type='application/pdf')
	
	# Optionally, set the content disposition to inline (to view in the browser)
	response['Content-Disposition'] = 'inline; filename="your_file.pdf"'
	
	return response
