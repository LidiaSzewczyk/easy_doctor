from django.urls import path

from . import views

app_name = 'visit'
urlpatterns = [
    path('', views.DiagnosisListView.as_view(), name='diagnosis_list'),
    path('<slug:slug>/', views.DiagnosisDetailView.as_view(), name='diagnosis_detail'),
]
