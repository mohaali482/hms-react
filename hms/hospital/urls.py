from unicodedata import name
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('search',views.search_patient, name='search'),
    path('patient/<str:id>', views.patientInfo, name='patientInfo')
]