from django.contrib.auth import logout as logout_
from django.shortcuts import redirect, render
# Create your views here.


def logout(request):
    logout_(request)
    return redirect('login')