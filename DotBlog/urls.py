"""bloggingwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home,
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from blog import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('blog/', views.homepage, name='homepage'),
    path('blog/<int:id>/', views.writings, name='writings'),
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name="aboutus"),
    path('privacy-policy', views.privacy,name="privacy"),
    path('faq',views.faq, name="faq"),
    path('authors/', views.authors, name = 'authors'),
   path('blog/create', views.create_blog, name='create_blog'),
]

urlpatterns = urlpatterns + staticfiles_urlpatterns()
