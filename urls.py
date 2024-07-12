"""
URL configuration for Petcare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('register/',views.Registerpage,name='register'),
    path('login/',views.LoginPage,name='login'),
    path('logout/',views.LogoutPage,name='logout'),
    path('petcare/',include('app1.urls')),
    # path('dashboard/',views.Dashboard,name='dashboard'),
    path("about",views.About,name='about'),
    path('services/',views.ServiceView.as_view(),name='service'),
    path("insurance",views.Insurance,name='insurance'),
    path("hostel",views.Hostel,name='hostel'),
    path("food",views.Food,name='food'),
    path("calculator",views.Calculator,name='calculator'),
    path("landing",views.Landing,name='landing'),
  
    


]

