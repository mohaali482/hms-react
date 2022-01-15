from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Regist.as_view(), name='home'),
    path('search',views.search_patient, name='search')
]