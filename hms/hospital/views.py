from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.template import context
from django.views.generic import CreateView
from django.core.exceptions import PermissionDenied

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
<<<<<<< HEAD
    return render(request,'hospital/search.html', context)


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

class Regist(RoleReceptionMixin, CreateView):
    form_class = RegisterPatientForm
    success_url = reverse_lazy('search')
    context_object_name = 'form'
    template_name = 'hospital/register.html'

    def get_context_data(self, **kwargs):
        kwargs['text'] = 'Add a Patient'
        kwargs['general'] = 'Patient Information'
        kwargs['reception'] = True
        return super().get_context_data(**kwargs)

    
=======
    return render(request,'hospital/registered-patient.html', context)
>>>>>>> 1fe5aea3dfa27d327ede13fa4e697d2d2e7f10ec
