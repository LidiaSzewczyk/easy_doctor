from django.contrib import admin

from visit.models import Diagnosis, Priority, Choice, Text, Part, FormType


class PriorityInline(admin.TabularInline):
    model = Priority
    show_change_link = True
    extra = 0
    fields = ['part', 'priority', 'text', 'diagnosis']


class ChoicesInline(admin.TabularInline):
    model = Choice
    show_change_link = True
    extra = 0
    fields = ['text', 'doctor_choice', 'patient_choice', 'priority']


class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'number', 'info', 'created_at')
    search_fields = ('name', 'number', 'info')
    list_display_links = ('id', 'name')
    prepopulated_fields = {'slug': ('number',)}
    inlines = [PriorityInline]


class PartAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    list_display_links = ('id', 'name')


class PriorityAdmin(admin.ModelAdmin):
    list_display = ('id', 'part', 'priority', 'diagnosis', 'text')
    search_fields = ('diagnosis__number', 'diagnosis__name', 'text__doctor_text')
    list_display_links = ('id', 'part')
    list_filter = ('part', 'priority')


class FormTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('name',)
    search_fields = ('name',)
    list_display_links = ('id', 'name')


class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'doctor_text', 'patient_text', 'form_type')
    list_filter = ('form_type',)
    search_fields = ('title', 'doctor_text', 'patient_text',)
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ['form_type']
    save_on_top = True
    inlines = [PriorityInline, ChoicesInline]


admin.site.register(Diagnosis, DiagnosisAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Part, PartAdmin)
admin.site.register(Priority, PriorityAdmin)
admin.site.register(FormType, FormTypeAdmin)
