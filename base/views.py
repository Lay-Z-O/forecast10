from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .forms import SignUpForm, LogInForm
from .models import UserProfile
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



# Create your views here.
def base(request):
    return render(request, 'base.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def home(request):
    return render(request, 'homepage.html')

def overview(request):
    return render(request, 'overview.html')

def forecast(request):
    return render(request, 'forecast.html')

def information(request):
    return render(request, 'information.html')

def profile(request):
    return render(request, 'profile.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = UserProfile.objects.get(username=username)
            except UserProfile.DoesNotExist:
                messages.error(request, 'User does not exist.')
                return render(request, 'log-in.html', {'form': form})
            
            if not check_password(password, user.password):
                messages.error(request, 'Incorrect password.')
                return render(request, 'log-in.html', {'form': form})
            
            # Log in the user (you may want to use Django's built-in login functionality)
            return redirect('overview')  # Replace 'home' with the desired URL after successful login
    else:
        form = LogInForm()
    return render(request, 'log-in.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home') 


