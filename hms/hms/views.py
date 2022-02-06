from django.contrib.auth import logout as logout_
from django.shortcuts import redirect, render
# Create your views here.

#defining our home page 
def home(request):
    return redirect('home-hospital')


#redirectng the user to login page after logout
def logout(request):
    logout_(request)
    return redirect('login')
