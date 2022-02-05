from ast import arg
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

def role_reception(request):
    try:
        if request.user.employee.get(user=request.user).role == "Reception":
            return True
        else:
            raise PermissionDenied
    except:
        return False


def role_doctor(request):
    try:
        if request.user.employee.get(user=request.user).role == "Doctor":
            return True
        else:
            raise PermissionDenied
    except:
        return False


@login_required
def home_hospital(request):
    try:
        if role_reception(request):
            return redirect('register')
        elif role_doctor(request):
            return redirect('doctorHome')
        else:
            raise PermissionDenied
    except:
        return HttpResponseForbidden


@login_required
def add_queue(request,id):
    if not role_reception(request):
        return redirect('home')
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
    if not role_reception(request):
        return redirect('home')
    context = {}
    context['text'] = 'Add a Patient'
    context['general'] = 'Patient Information'
    context['reception'] = True
    patients = Patient.objects.all()
    queue = []
    for items in Queue.objects.all():
        queue.append(items.get_patient())
    context['menuactive'] = 'managepatient'
    context['menuactivech'] = 'registeredpatient'
    context['patients'] = patients
    context['queue'] = queue
    
    return render(request,'hospital/registered-patient.html', context)

def queue_list(request):
    if not role_reception(request):
        return redirect('home')

    context = {}

    context['general'] = 'Patient Information'
    context['reception'] = True
    queue = []
    for items in Queue.objects.all():
        queue.append(items.get_patient())
    context['queue'] = queue
    context['menuactive'] = 'managequeue'
    return render(request,'hospital/manage-queue.html', context)

@login_required
def dequeue(request, id):
    if not role_reception(request):
        return redirect('home')

    patient = Patient.objects.get(id=id)

    queue = Queue.objects.get(patient = patient)
    queue.delete()

    messages.success(request, f'Removed {patient.full_name()} from the queue.')
    return redirect('search')

@login_required
def patientInfo(request, id):
    if not role_reception(request):
        return redirect('home')
    context = {}
    context['reception'] = True
    context['title'] = 'Patient Info'
    patient = Patient.objects.get(id = id)
    context['menuactive'] = 'managepatient'
    context['menuactivech'] = 'registeredpatient'
    context['patient'] = patient
    return render(request, 'hospital/patient-info.html', context)


@login_required
def doctor_home(request):
    if not role_doctor(request):
        return redirect('home')
    context = {}
    patients = []
    for patient in Queue.objects.all():
        patients.append(patient.patient)
    context['patients'] = patients
    context['doctor'] = True
    context['text'] = 'Queue'
    context['menuactivech'] = 'search'
    context['general'] = 'Waiting patients'
    return render(request, 'hospital/doctor-home.html', context)


@login_required
def patient_history(request, id):
    if not role_doctor(request):
        return redirect('home')
    context = {}
    context['reception'] = True
    context['title'] = 'Patient History'
    patient = Patient.objects.get(id = id)
    context['patient'] = patient
    return render(request, 'hospital/patient-history.html', context)


@login_required
def old_history(request, id):
    if not role_doctor(request):
        return redirect('home')
    patient = Patient.objects.get(id = id)
    history = PatientHistory.objects.filter(patient=patient)
    context = {}
    context['patient'] = patient
    context['condition'] = history
    context['menuactive'] = 'managepatient'
    context['menuactivech'] = 'registeredpatient'
    context['doctor'] = True

    return render(request,'hospital/view-history.html',context)


@login_required
def history_info(request, id):
    if not role_doctor(request):
        return redirect('home')
    history = PatientHistory.objects.get(id = id)
    context = {}
    context['patient'] = history.patient
    context['history'] = history
    context['menuactive'] = 'managepatient'
    context['menuactivech'] = 'registeredpatient'
    context['doctor'] = True

    return render(request, 'hospital/patient-history-detail.html', context)
    



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
    condition = None

    def get(self, request, *args, **kwargs):
        self.patient = Patient.objects.get(id = kwargs['id'])
        return super().get(request, *args, **kwargs)


    def get_context_data(self, **kwargs):
        kwargs['patient'] = self.patient
        kwargs['text'] = 'Add a Patient'
        kwargs['general'] = 'Patient Information'
        kwargs['menuactivech'] = 'edithistory'
        kwargs['doctor'] = True
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.patient = Patient.objects.get(id =self.kwargs['id'])
        messages.success(self.request, 'Condition Registered Successfully')
        response = super().form_valid(form)
        pk = form.instance.pk
        self.condition = Condition.objects.get(id = pk)
        patient_history_new = PatientHistory(patient = self.patient, conditions=self.condition)
        patient_history_new.save()
        
        return response


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
class PatientDeleteView(RoleReceptionMixin, DeleteView):
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

    def form_valid(self, form):
        messages.success(self.request, 'Patient Deleted Successfully')
        return super().form_valid(form)


@login_required
def register(response):
    if not role_reception(request):
        return redirect('home')
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