from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import login as django_login, logout as django_logout, authenticate as django_authenticate
# importing as such so that it doesn't create a confusion with our methods and django's default methods

from django.contrib.auth.decorators import login_required
from .forms import AuthenticationForm, RegistrationForm
from django.contrib import messages
from django.views.decorators.cache import never_cache


@never_cache
def login(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                email = request.POST['email']
                password = request.POST['password']
                user = django_authenticate(email=email, password=password)
                if user is not None:
                    if user.is_active:
                        django_login(request, user)
                        # user is redirected to dashboard
                        return redirect('home')
                else:
                    messages.error(request, 'username or password not correct')
                    return redirect('login')
        else:
            form = AuthenticationForm()
        page_title = 'Login Page'
        return render(request, 'accounts/login.html', {'form': form, 'page_title': page_title})


@never_cache
def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = RegistrationForm(data=request.POST)
            if form.is_valid():
                form.save()
                email = request.POST['email']
                password = request.POST['password1']
                username = request.POST['username']
                u = django_authenticate(
                    email=email, password=password, username=username)
                django_login(request, u)
                return redirect('home')
        else:
            form = RegistrationForm()
        page_title = 'Register Page'
        return render(request, 'accounts/signup.html', {'form': form, 'page_title': page_title})


@never_cache
def logout(request):
    django_logout(request)
    return redirect('home')


"""@login_required(login_url ="/")
def dashboard(request):
    return render(request, 'dashboard.html',{})"""

"""from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .models import CustomUser
from .forms import SignUpForm, LoginForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            CustomUser = form.save()
            CustomUser.refresh_from_db()  # load the profile instance created by the signal
            CustomUser.email = form.cleaned_data.get('email')
            CustomUser.save()
            raw_password = form.cleaned_data.get('password1')
            CustomUser = authenticate(
                username=CustomUser.username, password=raw_password)
            login(request, CustomUser)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})


def userlogin(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print('asdsad')
            username = form.cleaned_data.get('username')
            psw = form.cleaned_data.get('password')
            CustomUser = authenticate(
                username=username, password=psw)
            login(request, CustomUser)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})"""
