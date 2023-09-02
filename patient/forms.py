from django import forms

from .models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'birth_date', 'pesel', 'email', 'birth_date', 'address', 'phone')

        widgets = {el: forms.TextInput(attrs={'class': 'form-control'}) for el in fields}
