
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('',views.Homepage,name='Home'),
#     path("about",views.about,name='about'),
#     path("services",views.services,name='services'),
#     path("insurance",views.insurance,name='insurance'),

# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('',views.Homepage,name='Home'),
#     path("about",views.about,name='about'),
#     path("services",views.services,name='services'),
#     path("insurance",views.insurance,name='insurance'),

# ]
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns
    # urls.py
    path('process_payment/', views.process_payment, name='process_payment')

]
