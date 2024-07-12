# urls.py

from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Homepage, name='home'),
    path('accounts/', include('allauth.urls')),
    path('register/', views.Registerpage, name='register'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('services/', views.servicepage, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('doctor/', views.Doctor, name='doctor'),
    path('book/', views.Book, name='book'),
    path('hostelfacilities/', views.Hostelfacilities, name='hostelfacilities'),
    path('insurance/', views.Insurance, name='insurance'),
    path('food/', views.Food, name='food'),
    path('hostelbooking/', views.Hostelbooking, name='hostelbooking'),
    path('appointment/', views.Appointement, name='appointment'),
    path('payment/', views.payment, name='payment'),
    path('process_payment/', views.process_payment, name='process_payment'),
    path('doctorappointment/', views.DoctorAppointement, name='doctorappointment'),
    path('get_response/', views.get_response, name='get_response'),
    path('help/', views.Help, name='help'),
]
