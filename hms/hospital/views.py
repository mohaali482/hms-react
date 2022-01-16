from django.utils import timezone
from django import forms
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context
from .forms import *
# Create your views here.


def login(request):
    return render(request,'hospital/login.html')

def home(request):
    return render(request, 'hospital/dashboard.html')

def add_queue(request,id):
    patient = Patient.objects.get(id = id)
    new_queue = Queue(patient=patient)
    new_queue.save()

    return redirect('search')

def search_patient(request):
    context = {}
    context['text'] = 'Add a Patient'
    context['general'] = 'Patient Information'
    context['reception'] = True
    patients = Patient.objects.all()
    context['menuactive'] = 'managepatient'
    context['menuactivech'] = 'registeredpatient'
    context['patients'] = patients
    
    return render(request,'hospital/registered-patient.html', context)
def patientInfo(request, id):
    context = {}
    context['reception'] = True
    context['title'] = 'Patient Info'
    patient = Patient.objects.get(id = id)
    context['menuactive'] = 'managepatient'
    context['menuactivech'] = 'registeredpatient'
    context['patient'] = patient
    return render(request, 'hospital/patient-info.html', context)

def edit(request):
    context = {}
    context['text'] = 'Edit Patient Info'
    context['general'] = 'Patient Information'
    context['reception'] = True
    patients = Patient.objects.all()
    context['menuactive'] = 'managepatient'
    context['menuactivech'] = 'editpatient'
    context['patients'] = patients
    context['editing'] = True
    return render(request,'hospital/registered-patient.html', context)

def doctorHome(request):
    context = {}
    patients = []
    for patient in Queue.objects.all():
        patients.append(patient.patient)
    context['patients'] = patients
    context['Doctor'] = True
    context['text'] = 'Queue'
    context['menuactivech'] = 'search'
    context['general'] = 'Waiting patients'
    return render(request, 'hospital/doctor-home.html', context)
def patientHistory(request, id):
    context = {}
    context['reception'] = True
    context['title'] = 'Patient History'
    patient = Patient.objects.get(id = id)
    context['patient'] = patient
    return render(request, 'hospital/patient-history.html', context)

def old_history(request, id):
    patient = Patient.objects.get(id = id)
    history = PatientHistory.objects.filter(patient=patient)
    conditions =[]
    for date in history:
        conditions.append(date.conditions)
    return render(request,'hospital/view-history.html',{'patient':patient,'condition':conditions})

def condition_info(request, id):
    condition = Condition.objects.get(id = id)





class RoleReceptionMixin:

    def dispatch(self, request, *args, **kwargs):
        if request.user.employee.get(user=request.user).role == "Reception":
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

class RoleDoctorMixin:

    def dispatch(self, request, *args, **kwargs):
        if request.user.employee.get(user=request.user).role == "Doctor":
            return super().dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied

class Register(RoleReceptionMixin, CreateView):
    form_class = RegisterPatientForm
    success_url = reverse_lazy('search')
    context_object_name = 'form'
    template_name = 'hospital/register.html'

    def get_context_data(self, **kwargs):
        kwargs['text'] = 'Add a Patient'
        kwargs['general'] = 'Patient Information'
        kwargs['menuactive'] = 'managepatient'
        kwargs['menuactivech'] = 'newpatient'
        kwargs['reception'] = True
        return super().get_context_data(**kwargs)


class CreateCondition(CreateView):
    model = Condition
    form_class = RegisterPatientCondition
    success_url = reverse_lazy('doctorHome')
    context_object_name = 'form'
    template_name = 'hospital/patient-history.html'
    patient = None

    def get(self, request, *args, **kwargs):
        self.patient = Patient.objects.get(id = kwargs['id'])
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        kwargs['patient'] = self.patient
        kwargs['text'] = 'Add a Patient'
        kwargs['general'] = 'Patient Information'
        kwargs['menuactivech'] = 'edithistory'
        kwargs['Doctor'] = True
        return super().get_context_data(**kwargs)

class PatientUpdateView(UpdateView):
    model = Patient
    form_class = EditPatient
    template_name = "hospital/edit-patient.html"
    

    def get_context_data(self, **kwargs):
        kwargs['text'] = 'Add a Patient'
        kwargs['general'] = 'Patient Information'
        kwargs['menuactive'] = 'managepatient'
        kwargs['menuactivech'] = 'editpatient'
        kwargs['reception'] = True
        return super().get_context_data(**kwargs)

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST) 
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:   
        form = RegisterForm()

    return render(response, "./hospital/register.html",{"form": form})