from django.shortcuts import render
from . import models
from django.http import HttpResponse


def signup_views(request):
    return HttpResponse("Just to make sure the page is working")
