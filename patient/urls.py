from django.urls import path

from . import views

app_name = 'patient'
urlpatterns = [
    path('', views.PatientListView.as_view(), name='patient_list'),
    path('<int:pk>/', views.PatientDetailView.as_view(), name='patient_detail'),
    path('patient_create/', views.PatientCreateView.as_view(), name='patient_create'),
    path('<int:pk>/patient_update/', views.PatientUpdateView.as_view(), name='patient_update'),

]
