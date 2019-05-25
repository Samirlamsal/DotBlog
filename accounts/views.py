from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def signup_views(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/blog/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})


def login_views(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/blog/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_views(request):
    if request.method=='POST':
        logout(request)
        return redirect('/accounts/login/')

