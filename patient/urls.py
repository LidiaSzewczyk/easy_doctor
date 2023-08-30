from django.urls import path

from . import views

app_name = 'patient'
urlpatterns = [
    path('', views.PatientListView.as_view(), name='patient_list'),
    path('<int:pk>/', views.PatientDetailView.as_view(), name='patient_detail'),
]
