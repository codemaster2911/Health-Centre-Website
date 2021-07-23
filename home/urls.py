
from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vd/', views.vd, name='vd'),
    path('service/', views.service, name='service'),
    path('pappointment/', views.pappointment, name='pappointment'),
    path('home/', views.home, name='home'),
    path('phome/', views.phome, name='phome'),
    path('signup/',views.handleSignup,name='handleSignup'),
    path('login/',views.handleLogin,name='handleLogin'),
    path('logout/',views.handleLogout,name='handleLogout'),
    path('doctors/',views.doctors,name='doctors'),
    path('delete_data/<int:id>/',views.delete_data,name='delete_data'),
    path('<int:id>/',views.update_data,name='update_data'),
    path('appointment/',views.appointment,name='appointment'),
    path('delete_data2/<int:id>/',views.delete_data2,name='delete_data2'),
    path('ud2/<int:id>/',views.update_data2,name='update_data2'),
    path('patient/',views.patient,name='patient'),
    path('delete_data3/<int:id>/',views.delete_data3,name='delete_data3'),
    path('ud3/<int:id>/',views.update_data3,name='update_data3'),
]

