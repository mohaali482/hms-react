from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.utils import timezone
from django import forms
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import context
from .forms import *
from django.core.exceptions import PermissionDenied
# Create your views here.

@login_required
def home_hospital(request):
    try:
        if request.user.employee.get(user=request.user).role == "Reception":
            return redirect('register')
        elif request.user.employee.get(user=request.user).role == "Doctor":
            return redirect('doctorHome')
    except:
        return HttpResponseForbidden("403 Forbidden")


@login_required
def add_queue(request,id):
    patient = Patient.objects.get(id = id)
    if Queue.objects.filter(patient= patient):

        messages.warning(request, "Patient already in queue")
        return redirect('search')
    new_queue = Queue(patient=patient)
    new_queue.save()

    messages.success(request, f"Added {patient.full_name()} to the queue.")
    return redirect('search')


@login_required
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


@login_required
def patientInfo(request, id):
    context = {}
    context['reception'] = True
    context['title'] = 'Patient Info'
    patient = Patient.objects.get(id = id)
    context['menuactive'] = 'managepatient'
    context['menuactivech'] = 'registeredpatient'
    context['patient'] = patient
    return render(request, 'hospital/patient-info.html', context)


@login_required
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


@login_required
def patientHistory(request, id):
    context = {}
    context['reception'] = True
    context['title'] = 'Patient History'
    patient = Patient.objects.get(id = id)
    context['patient'] = patient
    return render(request, 'hospital/patient-history.html', context)


@login_required
def old_history(request, id):
    patient = Patient.objects.get(id = id)
    history = PatientHistory.objects.filter(patient=patient)
    conditions =[]
    for date in history:
        conditions.append(date.conditions)
    return render(request,'hospital/view-history.html',{'patient':patient,'condition':conditions})


@login_required
def condition_info(request, id):
    condition = Condition.objects.get(id = id)




@method_decorator(login_required, name = 'dispatch')
class RoleReceptionMixin:

    def dispatch(self, request, *args, **kwargs):
        try:
            if request.user.employee.get(user=request.user).role == "Reception":
                return super().dispatch(request, *args, **kwargs)
            else:
                raise PermissionDenied
        except:
            raise PermissionDenied


@method_decorator(login_required, name = 'dispatch')
class RoleDoctorMixin:

    def dispatch(self, request, *args, **kwargs):
        try:
            if request.user.employee.get(user=request.user).role == "Doctor":
                return super().dispatch(request, *args, **kwargs)
            else:
                raise PermissionDenied
        except:
            raise PermissionDenied


@method_decorator(login_required, name = 'dispatch')
class Register(RoleReceptionMixin, CreateView):
    form_class = RegisterPatientForm
    success_url = reverse_lazy('register')
    context_object_name = 'form'
    template_name = 'hospital/register.html'
    

    def get_context_data(self, **kwargs):
        kwargs['text'] = 'Add a Patient'
        kwargs['general'] = 'Patient Information'
        kwargs['menuactive'] = 'managepatient'
        kwargs['menuactivech'] = 'newpatient'
        kwargs['reception'] = True
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Patient Registered Successfully')
        return super().form_valid(form)


@method_decorator(login_required, name = 'dispatch')
class CreateCondition(RoleDoctorMixin,CreateView):
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

    def form_valid(self, form):
        messages.success(self.request, 'Condition Registered Successfully')
        return super().form_valid(form)


@method_decorator(login_required, name = 'dispatch')
class PatientUpdateView(RoleReceptionMixin, UpdateView):
    model = Patient
    form_class = EditPatient
    template_name = "hospital/edit-patient.html"
    success_url = reverse_lazy('search')
    

    def get_context_data(self, **kwargs):
        kwargs['text'] = 'Add a Patient'
        kwargs['general'] = 'Patient Information'
        kwargs['menuactive'] = 'managepatient'
        kwargs['menuactivech'] = 'registeredpatient'
        kwargs['reception'] = True
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        messages.success(self.request, 'Patient Information Updated Successfully')
        return super().form_valid(form)


@method_decorator(login_required, name = 'dispatch')

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = "hospital/delete_patient.html"
    success_url = reverse_lazy('search')

    def get_context_data(self, **kwargs):
        kwargs['text'] = 'Add a Patient'
        kwargs['general'] = 'Patient Information'
        kwargs['menuactive'] = 'managepatient'
        kwargs['menuactivech'] = 'registeredpatient'
        kwargs['reception'] = True
        return super().get_context_data(**kwargs)


@login_required
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST) 
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:   
        form = RegisterForm()

    return render(response, "./hospital/register.html",{"form": form}) 


class UpdateUserProfile(UpdateView):
    model = User
    form_class = UpdateProfileForm
    template_name = "hospital/updateprofile.html"

    def form_valid(self, form):
        messages.success(self.request, 'Updated User Data Successfully')
        return super().form_valid(form)