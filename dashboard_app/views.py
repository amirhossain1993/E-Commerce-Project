from django.shortcuts import render, redirect, get_object_or_404
from main_app.models import *
from dashboard_app.forms import *
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'dashboard/index.html')



# Product List Function
def product_list(request):
    products = Product.objects.all()
    return render(request, 'dashboard/products/product_list.html', {'products' : products })



# Product Add Function
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfuly.')
            return redirect('product_list')
    else:
        form = ProductForm()        
    return render(request, 'dashboard/products/product_add.html', {'form' : form})



# Product Editing Function
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfuly.')
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)        
    return render(request, 'dashboard/products/product_add.html', {'form' : form})


# Delete Product
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, 'Product delete successfuly.')
    return redirect('product_list')
    


