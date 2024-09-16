from django.urls import path
from main_app.views import *

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('product_detail/<int:pk>', product_detail, name='product_detail'),
    path('about/', about, name='about'),
    path('search/', product_search, name='product_search-page'),
    path('category_product/<int:pk>', category_product, name='category_product_page'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
]