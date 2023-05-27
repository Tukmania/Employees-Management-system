from django.urls import path
from . import views

urlpatterns = [
   
     path('',views.signup, name='signup'),
     path('sigin',views.signin, name='sigin'),
      path('signup_success',views.signin, name='sigin'),
      path('home',views.home,name='home'),
     
     
    
]