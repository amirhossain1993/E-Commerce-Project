from django.urls import path

from user_app.views import *

urlpatterns = [
    path('register_form/',register_form,name='register_form'),
    path('login_page/',login_page,name='login_page'),
    
    path('logout/', logout_view, name='logout_view'),
]