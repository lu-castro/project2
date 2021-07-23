from django.shortcuts import render
from .models import Post, Author

# Create your views here.

def Index(request):
    post=Post.objects.all()
    return render(request, "index.html",{"post" : post})

