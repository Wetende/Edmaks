from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('uProfile', views.uProfile, name='uProfile'),
    path('mProperties', views.mProperties, name='mProperties'),
    path('fProperties', views.fProperties, name='fProperties'),
    path('cPassword', views.cPassword, name='cPassword'),
    
   
]
