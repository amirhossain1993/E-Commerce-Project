from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
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



def category_product(request,pk):
    filtering = Category.objects.get(pk=pk)
    product_filter = Product.objects.filter(category=filtering.id)
    return render(request, 'main_app/category_product_show.html',{'product_filter':product_filter})




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



# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()
    
#     return redirect('/')



@login_required(login_url='login_page')
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('/')

@login_required(login_url='login_page')
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total = sum(item.product.regular_price * item.quantity for item in cart_items)
    return render(request, 'main_app/cart.html', {'cart_items': cart_items, 'total': total})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    Wishlist.objects.get_or_create(user=request.user, product=product)
    return redirect('/')

@login_required
def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'main_app/wishlist.html', {'wishlist_items': wishlist_items})