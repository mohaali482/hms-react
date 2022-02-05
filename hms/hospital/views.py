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


#we are defing the role of recptionist
def role_reception(request):
    try:
        if request.user.employee.get(user=request.user).role == "Reception":
            return True
        else:
            raise PermissionDenied
    except:
        return False






#we are defing the doctor role

def role_doctor(request):
    try:
        if request.user.employee.get(user=request.user).role == "Doctor":
            return True
        else:
            raise PermissionDenied
    except:
        return False






#we are defing the home hosptal page depending  on the role of the actor

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
        return redirect('home')





# we are adding the queue to the reciptonist and its functionalty and requiring login for it

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





# we are adding the search for the receptionist

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


# we are adding queue list

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




# we are adding dequeue which functions ass queue remover

@login_required
def dequeue(request, id):
    if not role_reception(request):
        return redirect('home')

    patient = Patient.objects.get(id=id)

    queue = Queue.objects.get(patient = patient)
    queue.delete()

    messages.success(request, f'Removed {patient.full_name()} from the queue.')
    return redirect('search')



# we are adding patientInfo to our views

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



# we are creating a doctor home page for our doctor and adding to it what is needed

@login_required
def doctor_home(request):
    if not role_doctor(request):
        return redirect('home')
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



#we are adding patient history for our doctor to Edit

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




#we are adding view history for our doctor

@login_required
def old_history(request, id):
    if not role_doctor(request):
        return redirect('home')
    patient = Patient.objects.get(id = id)
    history = PatientHistory.objects.filter(patient=patient)
    conditions =[]
    for date in history:
        conditions.append(date.conditions)
    return render(request,'hospital/view-history.html',{'patient':patient,'condition':conditions})



#we are adding condition for our doctor

@login_required
def condition_info(request, id):
    if not role_doctor(request):
        return redirect('home')
    condition = Condition.objects.get(id = id)




# we are making a mixin to define the receptionist role and make her page only accessable only for her

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



# we are creating a doctor mixin to define the doctor page and restrict him 

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




# we are defining who can register patients 

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





# we are defining creating conditions for patient and defining who can do it 

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

#we made a class here to update user info
class UpdateUserProfile(UpdateView):
    model = User
    form_class = UpdateProfileForm
    template_name = "hospital/updateprofile.html"

    def form_valid(self, form):
        messages.success(self.request, 'Updated User Data Successfully')
        return super().form_valid(form)