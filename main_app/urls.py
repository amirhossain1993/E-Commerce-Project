 
from django.urls import path
from main_app.views import index,contact

urlpatterns = [
    path('',index,name='index'),
    path('contact/',contact,name='contact'),
]