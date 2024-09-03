from django.urls import path
from main_app.views import *

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
    path('product_detail/<int:pk>', product_detail, name='product_detail'),
    path('about/', about, name='about'),
    path('search/', product_search, name='product_search-page'),
]