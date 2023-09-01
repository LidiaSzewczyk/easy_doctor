from django.contrib import admin

from .models import PatientVisit


class PatientVisitAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'created_at', 'diagnosis')
    list_filter = ('doctor',)
    search_fields = (
    'patient__first_name', 'patient__last_name', 'doctor__last_name', 'doctor__first_name', 'diagnosis')
    list_display_links = ('id', 'patient')
    save_on_top = True


admin.site.register(PatientVisit, PatientVisitAdmin)
