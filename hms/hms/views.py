from django.contrib.auth import logout as logout_
from django.shortcuts import redirect, render
# Create your views here.


<<<<<<< HEAD
def logout(request):
    logout_(request)
    return redirect('login')
=======
def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username, password)
        if user is not None:
            login()
        else:
            pass
    else:
        return render(request, 'hospital/login.html',{})
def logout(request):
    print('req')
>>>>>>> 1fe5aea3dfa27d327ede13fa4e697d2d2e7f10ec
