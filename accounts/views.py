from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.


def login_view(request):
    if request.method == "GET":
        return render(request, "accounts/login.html")
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("root:home")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("accounts:login")
        else:
            messages.error(request, "Invalid form data")
            return redirect("accounts:login")

    

def register_view(request):
    if request.method == "GET":
        return render(request, "accounts/register.html") 
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect("accounts:login")
        else:
            messages.error(request, "input data is not valid")
            redirect (request.path_info)


@login_required
def logout_view(request):
    logout(request)
    return redirect("root:home")
