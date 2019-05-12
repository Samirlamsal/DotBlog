from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns=[
    path('signup/', views.signup_views, name ='signup'),

]
