from django.shortcuts import render,redirect

from user_app.forms import RegisterForm

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth import logout

# Create your views here.

def register_form(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    else:
        form = RegisterForm()
    return render(request, 'user_app/registerform.html', {'form': form})

    
    

def login_page(request):
    if request.method =='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            # Return an 'invalid login' error message
            context = {
                'error_message' : 'Username or Password is incorrect!!!',
            }
            return render(request, 'user_app/login.html', context)
        
    return render(request, 'user_app/login.html')



def logout_view(request):
    logout(request)
    return redirect('/')

