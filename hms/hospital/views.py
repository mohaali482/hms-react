from django.shortcuts import render
from django.http import HttpResponse
from django.template import context
from .forms import *
# Create your views here.


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
    return render(request, 'hospital/base.html', context)