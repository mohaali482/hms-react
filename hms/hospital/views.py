from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from .forms import *
# Create your views here.


def login(request):
    return render(request,'hospital/login.html')

def home(request):
    return render(request, 'hospital/dashboard.html')
def index(request):
    form = RegisterPatientForm(request.POST or None)
    # if form.is_valid():
    #     return HttpResponse('done')

    context = {}
    context['form'] = form
    context['text'] = 'Add a Patient'
    context['general'] = 'Patient Information'
    context['reception'] = True
    context['general'] = 'Patient Information'
    return render(request, 'hospital/register.html', context)
def patients(request):
    context = {}
    context['reception'] = True
    # database access to all the patients
    # patients = access from database through model

    #add the retrieved patient to a patients key in the context dictionary
    # context['patients'] = patients
    
    return render(request, 'hospital/registered-patient.html', context)