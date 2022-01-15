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
    return render(request, 'hospital/register.html', context)

def search_patient(request):
    context = {}
    context['text'] = 'Add a Patient'
    context['general'] = 'Patient Information'
    context['reception'] = True
    patients = [
        {
            "id": "0023",
            "first_name": "first",
            "middle_name": "middle",
            "last_name": "last",
            "b_date": "12/03/1999",
            "phone": "+251 964352301",
            "email": "sample@gmail.com",
            "sex": "M",
            "blood_type": "A+"
        },
        {
            "id": "0013",
            "first_name": "first",
            "middle_name": "middle",
            "last_name": "last",
            "b_date": "12/03/1999",
            "phone": "+251 964352301",
            "email": "sample@gmail.com",
            "sex": "M",
            "blood_type": "A+"
        },
        {
            "id": "0003",
            "first_name": "first",
            "middle_name": "middle",
            "last_name": "last",
            "b_date": "12/03/1999",
            "phone": "+251 964352301",
            "email": "sample@gmail.com",
            "sex": "M",
            "blood_type": "A+"
        }
    ]
    context['patients'] = patients
    return render(request,'hospital/registered-patient.html', context)
def patientInfo(request, id):
    context = {}
    context['reception'] = True
    context['title'] = 'Patient Info'
    patient = {
        "id": id,
        "first_name": "first",
        "middle_name": "middle",
        "last_name": "last",
        "b_date": "12/03/1999",
        "phone": "+251 964352301",
        "email": "sample@gmail.com",
        "sex": "M",
        "blood_type": "A+"
    }
    context['patient'] = patient
    return render(request, 'hospital/patient-info.html', context)
def doctorHome(request):
    context = {}
    patients = [
        {
            "id": "0023",
            "first_name": "first",
            "middle_name": "middle",
            "last_name": "last",
            "b_date": "12/03/1999",
            "phone": "+251 964352301",
            "email": "sample@gmail.com",
            "sex": "M",
            "blood_type": "A+"
        },
        {
            "id": "0013",
            "first_name": "first",
            "middle_name": "middle",
            "last_name": "last",
            "b_date": "12/03/1999",
            "phone": "+251 964352301",
            "email": "sample@gmail.com",
            "sex": "M",
            "blood_type": "A+"
        },
        {
            "id": "0003",
            "first_name": "first",
            "middle_name": "middle",
            "last_name": "last",
            "b_date": "12/03/1999",
            "phone": "+251 964352301",
            "email": "sample@gmail.com",
            "sex": "M",
            "blood_type": "A+"
        }
    ]
    context['patients'] = patients
    context['doctor'] = True
    context['text'] = 'Queue'
    context['general'] = 'Waiting patients'
    return render(request, 'hospital/doctor-home.html', context)
def patientHistory(request, id):
    context = {}
    context['reception'] = True
    context['title'] = 'Patient History'
    patient = {
        "id": id,
        "first_name": "first",
        "middle_name": "middle",
        "last_name": "last",
        "b_date": "12/03/1999",
        "phone": "+251 964352301",
        "email": "sample@gmail.com",
        "sex": "M",
        "blood_type": "A+"
    }
    context['patient'] = patient
    return render(request, 'hospital/patient-history.html', context)