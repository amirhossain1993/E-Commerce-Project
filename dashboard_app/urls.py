from django.urls import path
from dashboard_app.views import *

urlpatterns = [
    path('dashboard/',index,name='index'),
    
    path('product_list/',product_list,name='product_list'),
    path('add_product/',add_product,name='add_product'),
    path('products/edit/<int:pk>',product_edit,name='product_edit'),
    path('products/delete/<int:pk>/', product_delete, name='product_delete'),
    
    
    
]