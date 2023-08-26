from django.contrib import admin

from visit.models import Diagnosis


class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'info', 'created_at')
    search_fields = ('name', 'number', 'info')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('number',)}


admin.site.register(Diagnosis, DiagnosisAdmin)
