from django.urls import path
from django.contrib.auth import views as auth_views
from user_app.views import *

urlpatterns = [
    path('register_form/',register_form,name='register_form'),
    path('login_page/',login_page,name='login_page'),
    path('logout/', logout_view, name='logout_view'),
    
    
    path('profile/', profile, name='profile_page'),
    path('profile/update/', profileupdate, name='profileupdat_page'),
    
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='user_app/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='user_app/password_change_done.html'), name='password_change_done'),
    
    
]