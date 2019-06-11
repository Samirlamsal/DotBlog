from django.shortcuts import render, redirect
from .models import Article
#from .models import Author
from django.contrib import messages
#from  django.db import Q
from django.contrib.auth.decorators import login_required
from . import forms




def homepage(request):
    articles = Article.objects.all()
    return render(request, 'homepage.html', {'articles':articles})


def writings(request, id):
    material = Article.objects.get(id=id)
    return render(request, 'writings.html', {'material':material})


def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'about_us.html')

def privacy (request):
    return render(request, 'privacy.html')

def faq (request):
    return render(request, 'faq.html')


"""def search(request):
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = utils.get_query(query_string, ['title', 'author',])
        posts = Post.objects.filter(entry_query).order_by('created')
        return render(request, 'base.html', { 'query_string': query_string, 'posts': posts })
    else:
        return render(request, 'base.html', { 'query_string': 'Null', 'found_entries': 'Enter a search term' })
"""

@login_required(login_url="/accounts/login")
def create_blog(request):
    if request.method =='POST':
        form = forms.CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            #saving the forms
            instance = form.save(commit=False)   #Doesnt save instantly but is refering to a variable
            instance.author = request.user       #selecting the exact same loggedin author for the article
            instance.save()                      #finally saving the article
            return redirect('/blog/')
    else:
        form = forms.CreateBlog()
    return render(request, 'add_article.html', {'form':form})
