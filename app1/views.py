# views.py

from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
import re
from app1.models import PetInsurance
from .forms import BookingForm, HostelForm, ContactForm, PetInsuranceForm
from transformers import AutoModelForCausalLM, AutoTokenizer
import requests

# Load the conversational model and tokenizer
model_name = "microsoft/DialoGPT-medium"  # Example model

try:
    model = AutoModelForCausalLM.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
except (requests.ConnectionError, requests.exceptions.ConnectionError) as e:
    print(f"Failed to download the model: {e}")
    model = None
    tokenizer = None

def servicepage(request):
    return render(request, 'services.html')

def Homepage(request):
    return render(request, 'landing.html')

@csrf_protect
def about(request):
    return render(request, 'about.html')

def insurance(request):
    return render(request, 'insurance.html')

@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message is sent.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the phone number.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def Hostelbooking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking successfully created.')
            return redirect('services')
        else:
            messages.error(request, 'Please correct the phone number.')
    else:
        form = BookingForm()
    return render(request, 'services.html', {'form': form})

def Help(request):
    return render(request, 'help.html')

def Doctor(request):
    return render(request, 'doctor.html')

def DoctorAppointement(request):
    return render(request, 'doctorappointment.html')

def Appointement(request):
    if request.method == 'POST':
        form = HostelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Appointment successfully created.')
            return redirect('appointment')  # Redirect to the next page
        else:
            messages.error(request, 'Please correct the phone number.')
    else:
        form = HostelForm()
    return render(request, 'services.html', {'form': form})

def Booking(request):
    return render(request, 'booking.html')

def Insurance(request):
    return render(request, 'insurance.html')

def Hostelfacilities(request):
    return render(request, 'hostel.html')

def Food(request):
    return render(request, 'food.html')

def Book(request):
    return render(request, 'book.html')

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")
    return render(request, 'login.html')

def Registerpage(request):
    def is_strong_password(password):
        # Check for at least 8 characters
        if len(password) < 8:
            return False

        # Check for at least one uppercase letter
        if not any(char.isupper() for char in password):
            return False

        # Check for at least one lowercase letter
        if not any(char.islower() for char in password):
            return False

        # Check for at least one digit
        if not any(char.isdigit() for char in password):
            return False

        # Check for the presence of a special character (symbol)
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False

        return True

    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not the same!!")
        elif not is_strong_password(pass1):
            return HttpResponse("Your password does not meet the strength criteria. It should include a combination of uppercase letters, lowercase letters, numbers, and symbols.")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'register.html')

def payment(request):
    return render(request, 'payment.html')

def LogoutPage(request):
    logout(request)
    return redirect('home')

def process_payment(request):
    if request.method == 'POST':
        form = PetInsuranceForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            print(form.errors)
            return JsonResponse({'status': 'error'})
    return JsonResponse({'status': 'error'})

@csrf_exempt
def get_response(request):
    if model is None or tokenizer is None:
        return JsonResponse({'answer': 'The model is currently unavailable. Please try again later.'})

    if request.method == "GET":
        user_message = request.GET.get('question', '')
        
        # Predefined answers
        predefined_answers = {
            "When are doctors available?": "Doctors are available from 10 AM to 5 PM.",
            "How many doctors are available each day?": "4 doctors are available each day.",
            "How many tickets do doctors have each day?": "Doctors have 20 tickets each day.",
            "What services do you offer?": "We offer medical consultation, diagnosis, and treatment services.",
            "Can I book an appointment?": "Yes, you can book an appointment through our website.",
            "What is your location?": "We are located at 123 Main Street, Kathmandu.",
            "How can I contact support?": "You can contact support via email at support@example.com."
        }
        
        # Check if user_message matches a predefined answer
        if user_message in predefined_answers:
            response = predefined_answers[user_message]
        else:
            # Generate a dynamic response from the chatbot model
            inputs = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors='pt')
            outputs = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)
            generated_response = tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Clean up the generated response
            cleaned_response = cleanup_response(user_message, generated_response)
            
            response = cleaned_response
        
        return JsonResponse({'answer': response})

def cleanup_response(user_message, generated_response):
    # Remove user input from the generated response
    pattern = re.escape(user_message)
    cleaned_response = re.sub(rf"{pattern}\s*", "", generated_response)
    
    # Trim any leading or trailing spaces and punctuation
    cleaned_response = cleaned_response.strip(" ?!,.")
    
    return cleaned_response
