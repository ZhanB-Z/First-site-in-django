from django.shortcuts import render, redirect
from .forms import RegisterForm
# Create your views here.


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/home") #this line allows us to redirect users to the home page after creating a new account
    else:
        form = RegisterForm() #this is a prebuilt form for creation of a new user

    return render(response, "register/register.html", {"form": form})