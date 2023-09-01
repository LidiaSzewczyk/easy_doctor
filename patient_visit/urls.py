from django.urls import path

from . import views

app_name = 'patient_visit'
urlpatterns = [
    path('', views.PatientVisitListView.as_view(), name='patient_visit_list'),
    path('<int:pk>/', views.PatientVisitDetailView.as_view(), name='patientvisit_detail'),

]
