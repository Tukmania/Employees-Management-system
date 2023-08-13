from django.urls import path
from . import views

# app_name = 'employee'

urlpatterns = [
   
     path('',views.signup, name='signup'),
     path('sigin',views.signin, name='sigin'),
      # path('signup_success',views.signin, name='sigin'),
      # path('home',views.home,name='home'),
      path('home',views.home,name='home'),
      path('add_employee',views.add_employee, name='add_employee'),
      path('update_employee/<int:employee_id>/', views.update_employee, name='update_employee'),
       path('remove_employee/<int:employee_id>/', views.remove_employee, name='remove_employee'),
       path('send_email_password' , views.send_email_password, name='send_email_password' ),
       path('add_asset',views.add_asset,name='add_asset'),
       path('assign_asset',views.assign_asset,name='assign_asset'),
      path('employee_list',views.employee_list, name = 'employee_list'),
      path('employee_assets/<int:employee_id>/', views.employee_assets, name='employee_assets')
      
     
     
    
]