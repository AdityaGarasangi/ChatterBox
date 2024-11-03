from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View


def register(request):
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            return redirect("login")
    else:
        user_form = RegisterForm()

    return render(
        request,
        "users/register.html",
        {
            "user_form": user_form,
        },
    )


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data["username"], password=data["password"]
            )
            if user is not None:
                login(request, user)
                return redirect("index")
            else:
                return HttpResponse("Invalid Credentials")
    else:
        form = LoginForm()
    return render(request, "users/login.html", {"form": form})


@login_required
def user_profile(request):
    return render(request, "users/profile.html")


class CustomLogoutView(View):
    def get(self, request):
        return render(
            request, "users/logout.html"
        )  # Render the logout confirmation template

    def post(self, request):
        logout(request)  # Log the user out
        return redirect("index")  # Redirect to the home page
