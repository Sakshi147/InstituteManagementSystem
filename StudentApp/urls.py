from django.urls import path

from StudentApp import views

urlpatterns=[
    path('',views.log_fun,name='log'),  # it will display login.html page
    path('logdata',views.logdata_fun),  # it will read data and verify

    path('reg',views.reg_fun,name='reg'),  # it will redirect to register.html page
    path('regdata',views.regdata_fun),  # it will create a superuser account

    path('home',views.home_fun,name='home'), # it will redirect home.html
    path('add_students',views.addstudent_fun,name='add'), # it will redirect addstudent.html
    path('readdata', views.readdata_fun),

    path('display',views.display_fun,name='display'), #it will display student table data in display.html
    path('update/<int:id>', views.update_fun,name='up'),
    path('delete/<int:id>',views.delete_fun,name='del'),
    path('log_out',views.log_out_fun,name='log_out')
]