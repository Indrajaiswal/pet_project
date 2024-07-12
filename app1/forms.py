from django.forms import ModelForm
from .models import Contact
from .models import Booking
from .models import Hostelbooking
from .models import Registration
from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.forms import UserCreationForm




class BookingForm(forms.ModelForm):
    # Define a RegexValidator for the phone number
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits and contain only numbers.",
    )

    # Use the RegexValidator for the phonenumber field
    phonenumber = forms.CharField(validators=[phone_regex])

    class Meta:
        model = Booking
        fields = ['fullname', 'petname', 'email', 'phonenumber', 'booking_date','booking_time']



class HostelForm(forms.ModelForm):
    # Define a RegexValidator for the phone number
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits and contain only numbers.",
    )

    # Use the RegexValidator for the phonenumber field
    phonenumber = forms.CharField(validators=[phone_regex])

    class Meta:
        model = Hostelbooking
        fields = ['fullname','petname','email','phonenumber','booking_from','booking_to']
        


class ContactForm(ModelForm):
     # Define a RegexValidator for the phone number
    phone_regex = RegexValidator(
        regex=r'^\d{10}$',
        message="Phone number must be 10 digits and contain only numbers.",
    )

    # Use the RegexValidator for the phonenumber field
    phonenumber = forms.CharField(validators=[phone_regex])
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phonenumber', 'message_text']

class RegistrationForm(UserCreationForm):
    class Meta:
        model = Registration
        fields = ('username', 'email', 'password1', 'password2')


# forms.py
from django import forms
from .models import PetInsurance

class PetInsuranceForm(forms.ModelForm):
    class Meta:
        model = PetInsurance
        fields = ['pet_name', 'owner_name', 'insurance_name', 'start_date']
