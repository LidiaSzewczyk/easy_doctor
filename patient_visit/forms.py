from django import forms

from patient.models import Patient
from .models import PatientVisit

patients_choices = Patient.objects.filter(doctor_id=2)


class PatientVisitForm(forms.ModelForm):
    class Meta:
        model = PatientVisit
        fields = ('patient', 'diagnosis', 'interview', 'examination', 'recommendations')

        widgets = {
            'patient': forms.Select(
                attrs={'choices': 'patients_choices', 'class': "form-select", 'aria-label': "Default select example"}),
            'diagnosis': forms.Textarea(
                attrs={'class': 'my-form-control', 'id': "diagn", 'type': "text", 'rows': '2', 'cols': '55'}),
            'interview': forms.Textarea(
                attrs={'class': 'my-form-control', 'id': "wywiad", 'type': "text", 'rows': '10', 'cols': '55'}),
            'examination': forms.Textarea(
                attrs={'class': 'my-form-control', 'id': "badanie", 'type': "text", 'rows': '10', 'cols': '55'}),
            'recommendations': forms.Textarea(
                attrs={'class': 'my-form-control', 'id': "zalecenia", 'type': "text", 'rows': '10', 'cols': '55'}),
        }


class PatientVisitUpdateForm(forms.ModelForm):
    class Meta:
        model = PatientVisit
        fields = ( 'diagnosis', 'interview', 'examination', 'recommendations')

        widgets = {
            'diagnosis': forms.Textarea(
                attrs={'class': 'my-form-control',  'type': "text", 'rows': '2', 'cols': '55'}),
            'interview': forms.Textarea(
                attrs={'class': 'my-form-control', 'type': "text", 'rows': '10', 'cols': '55'}),
            'examination': forms.Textarea(
                attrs={'class': 'my-form-control', 'type': "text", 'rows': '10', 'cols': '55'}),
            'recommendations': forms.Textarea(
                attrs={'class': 'my-form-control', 'type': "text", 'rows': '10', 'cols': '55'}),
        }