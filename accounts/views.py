from django.shortcuts import render, redirect
from . import models
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


def signup_views(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:writings')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})
