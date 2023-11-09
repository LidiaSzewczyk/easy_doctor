from django.urls import path

from . import views

app_name = 'patient_visit'
urlpatterns = [
    path('', views.PatientVisitListView.as_view(), name='patientvisit_list'),
    path('<int:pk>/', views.PatientVisitDetailView.as_view(), name='patientvisit_detail'),
    path('<int:pk>/update/', views.PatientVisitUpdateView.as_view(), name='patientvisit_update'),
    path('<int:pk>/delete/', views.PatientVisitDeleteView.as_view(), name='patientvisit_delete'),
    path('<int:pk>/pdf/', views.export_visit_to_pdf, name='patientvisit_pdf'),
]
