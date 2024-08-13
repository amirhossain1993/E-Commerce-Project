from django.shortcuts import render,redirect
from main_app.forms import *

# Create your views here.


def index (request):
    banner = Banner.objects.all()
    
    context = {
        'banner' : banner,
    }
    return render(request, 'main_app/index.html', context)


def contact (request):
    if request.method == 'POST':                
        form = Contactfrom (request.POST)        
        if form.is_valid():     
            form.save()        
            return redirect('index')  

    else:
        form = Contactfrom()
    return render(request, 'main_app/contact.html',{'form':form})
