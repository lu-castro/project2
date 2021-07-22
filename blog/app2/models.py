from typing import Text
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    image=models.ImageField(upload_to='image', blank=True)
    title=models.CharField(max_length=50, null=False)
    text=models.TextField(blank=False)
    date=models.DateField(auto_now=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.SlugField()
    def __str__(self):
        return self.title

class Author(models.Model):
    f_name=models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    


