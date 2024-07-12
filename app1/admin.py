from django.contrib import admin
from .models import Contact
from .models import Booking
from .models import Hostelbooking

admin.site.register(Contact)
admin.site.register(Booking)
admin.site.register(Hostelbooking)
