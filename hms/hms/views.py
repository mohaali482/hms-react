from django.contrib.auth import logout as logout_
from django.shortcuts import redirect, render
# Create your views here.


def home(request):
    return redirect('login')

def logout(request):
    logout_('home')
    return redirect('login')
