from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'hospital/dashboard.html')
def index(request):
    return render(request, 'hospital/base.html')