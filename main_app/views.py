from django.shortcuts import render,redirect
from main_app.forms import *

# Create your views here.


def index (request):
    banner = Banner.objects.all()
    category = Category.objects.all()
    brand = Brand.objects.all() 
    product = Product.objects.all()  
    
    context = {
        'banner' : banner,
        'category' : category,
        'brand' : brand,
        'product' : product,
    }
    return render(request, 'main_app/index.html', context)




def product_detail (request,pk):
    product = Product.objects.get(pk=pk)  
    
    context = {
        'product' : product,
    }     
    return render(request, 'main_app/product.html', context)






def contact (request):
    if request.method == 'POST':                
        form = Contactfrom (request.POST)        
        if form.is_valid():     
            form.save()        
            return redirect('index')  

    else:
        form = Contactfrom()
    return render(request, 'main_app/contact.html',{'form':form})
