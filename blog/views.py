from django.shortcuts import render
from .models import Article


def homepage(request):
    articles = Article.objects.all()
    return render(request, 'homepage.html', {'articles':articles})


def writings(request, id):
    material = Article.objects.get(id=id)
    return render(request, 'writings.html', {'material':material})
