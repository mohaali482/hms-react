from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home_hospital,name='home-hospital'),
    path('register/', views.Register.as_view(), name='register'),
    path('search',views.search_patient, name='search'),
    path('patient/<str:id>', views.patientInfo, name='patientInfo'),
    path('queue/<str:id>', views.add_queue, name='add_queue'),
    path('delete-patient/<pk>', views.delete_patient, name= 'delete-patient'),
    path('edit', views.edit, name='edit'),
    path('edit/<pk>', views.PatientUpdateView.as_view(), name='edit-patient'),
    path('patient-history/<str:id>', views.CreateCondition.as_view(), name='patientHistory'),
    path('old-history/<str:id>', views.old_history, name='old_history'),
    path('condition-info/<str:id>', views.condition_info, name='condition_info'),
    path('doctor/', views.doctorHome, name="doctorHome")
]