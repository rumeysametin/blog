from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ArticleForm
from .models import Article
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles":articles
    }
    return render(request, "dashboard.html", context)

def addarticle(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        
        messages.success(request, "You have successfully created an article")
        return redirect("index")
        
    return render(request, "addarticle.html", {"form":form})

def detail(request, id):
    article = Article.objects.filter(id = id).first()
    return render(request, "detail.html", {"article": article})
