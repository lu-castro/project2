from django.shortcuts import render
from .models import Post

# Create your views here.

def Index(request):
    post=Post.objects.all()
    return render(request, "index.html",{"post" : post})

def About(request):
    return render(request, "about.html", {})

def News(request):
    return render(request, "news.html", {})

