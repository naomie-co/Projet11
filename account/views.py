"""Account views of the pur beurre website"""

from django.shortcuts import render
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError


class ConnexionForm(forms.Form):
    """Creates a login form"""
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class SignupForm(forms.Form):
    """Create a sign up form"""
    email = forms.EmailField(label="Email", widget=forms.EmailInput)
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

def log_in(request):
    """Log in function"""

    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
            else: # error message
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'account/log_in.html', locals())


def log_out(request):
    """Log out function"""
    logout(request)
    return render(request, 'search/index.html')


def sign_up(request):
    """Sign up view"""
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            try:
                User.objects.create_user(username=username, email=email, password=password)
                userid = authenticate(request, username=username, password=password)
                login(request, userid)
            except IntegrityError:
                error = True #variable to print an error message if the username already exists
                form = SignupForm()
    else:
        form = SignupForm()
    return render(request, 'account/sign_up.html', locals())
