import io
import os
import datetime

from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin

from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Spacer
from reportlab.platypus import SimpleDocTemplate

from config.settings import BASE_DIR

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
		context["age_now"] = calc_age(self.object.patient.birth_date, datetime.date.today())
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
		context["age_now"] = calc_age(self.object.patient.birth_date, datetime.date.today())
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


def export_visit_to_pdf(request, pk):
	visit = PatientVisit.objects.filter(pk=pk).prefetch_related('patient')
	if len(visit) < 1:
		return HttpResponseForbidden()
	visit_values = visit.values()[0]
	visit_date = visit_values['start_date'].strftime("%d.%m.%Y  %H:%M")
	patient_name = visit[0].patient.get_full_name()
	
	# zarejestrowanie styli używanych w pdf
	pdfmetrics.registerFont(
		TTFont('Roboto-Thin', os.path.join(BASE_DIR, 'styles', 'fonts', 'RobotoCondensed-Regular.ttf')))
	pdfmetrics.registerFont(
		TTFont('Roboto-Bold', os.path.join(BASE_DIR, 'styles', 'fonts', 'RobotoCondensed-Bold.ttf')))
	sample_style_sheet = getSampleStyleSheet()
	headline1_style = sample_style_sheet["Heading1"]
	headline1_style.fontName = 'Roboto-Bold'
	title_style = sample_style_sheet["Title"]
	title_style.fontName = 'Roboto-Thin'
	body_text_style = sample_style_sheet["BodyText"]
	body_text_style.fontName = 'Roboto-Thin'
	body_text_style.bulletFontName = 'Roboto-Bold'
	
	'''Tworzenie dokumentu'''
	buf = io.BytesIO()
	doc = SimpleDocTemplate(buf, pagesize=A4, allowSplitting=False, title=patient_name + ' ' + visit_date)
	
	pdf_content = []
	
	'''Dodawanie tytułu do dokumentu'''
	paragraph_1 = Paragraph(f"{patient_name} - wizyta z dnia {visit_date}", title_style)
	pdf_content.append(paragraph_1)
	pdf_content.append(Spacer(10, 10))
	
	'''Dodawanie części wizyty do dokumentu'''
	
	age_visit_calc = calc_age(visit[0].patient.birth_date, visit_values['start_date'].date())
	age_visit = ''
	for label, amount in age_visit_calc.items():
		if amount != 0:
			age_visit += str(amount) + ' ' + label + ' '
	
	basic_paragraph = Paragraph(age_visit, body_text_style, bulletText="Wiek w dniu wizyty")
	pdf_content.append(basic_paragraph)
	
	pdf_content.append(Spacer(10, 10))
	
	visit_fields_dict = {'diagnosis': 'Rozpoznanie', 'interview': 'Wywiad', 'examination': 'Badanie',
						 'recommendations': 'Zalecenia'}
	
	for field_name in visit_fields_dict.keys():
		if field_name in visit_values.keys():
			line = visit_fields_dict[field_name]
			combined_basic_text_line = '  ' + str(visit_values[field_name])
			basic_paragraph = Paragraph(combined_basic_text_line, body_text_style, bulletText=line)
			pdf_content.append(basic_paragraph)
		
		pdf_content.append(Spacer(10, 10))
	
	basic_paragraph = Paragraph(visit[0].doctor.get_full_name(), body_text_style, bulletText="Lekarz")
	pdf_content.append(basic_paragraph)
	
	basic_paragraph = Paragraph(visit_values['updated_at'].strftime("%d.%m.%Y  %H:%M"), body_text_style,
								bulletText="Ostatnia modyfikacja")
	pdf_content.append(basic_paragraph)
	
	pdf_content.append(Spacer(10, 10))
	
	'''Budowanie dokumentu z elementami stałymi na każdej stronie'''
	doc.build(pdf_content, onFirstPage=add_to_first_page, onLaterPages=add_to_later_pages)
	buf.seek(0)
	
	'''tworzenie nazwy pliku'''
	filename = f"Wizyta {patient_name} {visit_date}.pdf"
	response = HttpResponse(buf, content_type='application/pdf')
	response["Content-Disposition"] = f'inline; filename={filename}'
	
	return response
