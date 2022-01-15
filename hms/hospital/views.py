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
    context['reception  '] = True
    return render(request, 'hospital/register.html', context)