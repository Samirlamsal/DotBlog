from django.shortcuts import render
from .models import Article
from .models import Author


def homepage(request):
    articles = Article.objects.all()
    return render(request, 'homepage.html', {'articles':articles})


def writings(request, id):
    material = Article.objects.get(id=id)
    return render(request, 'writings.html', {'material':material})

def authors(request):
    writers = Author.objects.all()
    return render(request, 'authors.html', {'writers':writers})

def Hall_of_fame(request, id):
    lekhak = Author.objects.get(id=id)
    return render(request, 'writers.html', {'lekhak':lekhak})
