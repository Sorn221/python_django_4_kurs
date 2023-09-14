from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Blog_post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class BlogListView(ListView):
    model = Blog_post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Blog_post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Blog_post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Blog_post
    fields = ['title', 'body']
    template_name = 'post_edit.html'

class BlogDeleteView(DeleteView):
    model = Blog_post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
