from django.shortcuts import render,redirect
from django.db.models import Q
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
    
    related_products = Product.objects.filter(category=product.category).exclude(id=product.pk).order_by('?')[:11]
    
    context = {
        'product' : product,
        'related_products' : related_products
    }     
    return render(request, 'main_app/product.html', context)



def product_search(request):
    query = request.GET.get('q', '')
    lookup = (
        Q(name__icontains=query) |
        Q(brand__name__icontains=query)
    )
    search_product = Product.objects.filter(lookup)

    context = {
        'search_product': search_product
    }
    return render(request, 'main_app/product_search.html', context)






def contact (request):
    if request.method == 'POST':                
        form = Contactfrom (request.POST)        
        if form.is_valid():     
            form.save()        
            return redirect('index')  

    else:
        form = Contactfrom()
    return render(request, 'main_app/contact.html',{'form':form})


def about(request):
    return render(request, 'main_app/about.html')