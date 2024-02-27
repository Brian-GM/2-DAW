from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


def signup(request):
    if request.user.is_authenticated:
        return redirect(reverse("memora:index"))
    if request.POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("memora:index"))
    else:
        form = SignupForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_user(request):
    error = ""

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user=user)
                return redirect(reverse("memora:index"))
            else:
                error = "Algo ta mal"
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form, "error": error})


def logout_user(request):
    logout(request)
    return render(request, "accounts/logout.html")


# Create your views here.
