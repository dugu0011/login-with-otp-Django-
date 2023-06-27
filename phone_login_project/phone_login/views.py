from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from .models import PhoneNumbers
from .utils import generate_otp, send_otp


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            otp = generate_otp()  # Generate OTP
            send_otp(phone_number, otp)  # Send OTP to the phone number

            user, created = PhoneNumbers.objects.get_or_create(
                phone_number=phone_number)
            user.otp = otp
            user.save()

            # Store the user's ID in the session
            request.session['user_id'] = user.id

            return redirect('verify_otp')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def verify_otp(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = PhoneNumbers.objects.get(id=user_id)

    if request.method == 'POST':
        entered_otp = request.POST['otp']
        if entered_otp == user.otp:
            user.is_verified = True
            user.save()

            # Remove user ID from the session
            del request.session['user_id']

            # Perform login action here (e.g., create a user session)

            return redirect('home')
        else:
            messages.error(request, 'Invalid OTP. Please try again.')

    return render(request, 'verify_otp.html')


def home(request):
    return render(request, 'home.html')
