from django.shortcuts import render,redirect

from user_app.forms import RegisterForm

from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect, HttpResponse

from django.contrib.auth import logout


from user_app.forms import *
from django.contrib import messages

# Create your views here.

def register_form(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_page')
        
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




def profileupdate(request):
    if request.method == 'POST':
        user_form = UserUpdate(request.POST, instance=request.user)
        profile_form = ProfileUpdate(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.info(request, 'Profile details updated.')
            return redirect('profile_page')
    else:
        user_form = UserUpdate(instance=request.user)
        profile_form = ProfileUpdate(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'user_app/profileupdate.html', context)

def profile(request):
        return render (request, 'user_app/profile.html')