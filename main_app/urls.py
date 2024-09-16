from django.urls import path
from main_app.views import *

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('about/', about, name='about'),
    
    path('product_detail/<int:pk>', product_detail, name='product_detail'),
    path('search/', product_search, name='product_search-page'),
    path('category_product/<int:pk>', category_product, name='category_product_page'),
    
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('increment_cart/<int:item_id>/', increment_cart_item, name='increment_cart_item'),
    path('decrement_cart/<int:item_id>/', decrement_cart_item, name='decrement_cart_item'),
    path('cart/', cart, name='cart'),
    
    path('add_to_wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', wishlist, name='wishlist'),
    
    path('checkout/', checkout, name='checkout')
]