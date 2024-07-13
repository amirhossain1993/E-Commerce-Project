from django.shortcuts import render,redirect
from main_app.forms import Contactfrom

# Create your views here.


def index (request):
    return render(request, 'main_app/index.html')


def contact (request):
    if request.method == 'POST':                
        form = Contactfrom (request.POST)        
        if form.is_valid():     
            form.save()        
            return redirect('index')  

    else:
        form = Contactfrom()
    return render(request, 'main_app/contact.html',{'form':form})
