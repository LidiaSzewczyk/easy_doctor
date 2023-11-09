from django.contrib import admin

from .models import Patient


class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_full_name', 'birth_date', 'doctor')
    list_filter = ('doctor',)
    search_fields = ('first_name', 'last_name', 'doctor__last_name', 'doctor__first_name',)
    list_display_links = ('id', 'get_full_name')
    save_on_top = True



admin.site.register(Patient, PatientAdmin)
