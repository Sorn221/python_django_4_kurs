from django.shortcuts import render
from django.views.generic import ListView
from . models import Blog_post

class BlogListView(ListView):
    model = Blog_post
    template_name = 'home.html'
