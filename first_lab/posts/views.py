from django.shortcuts import render
from  django.views.generic import ListView
from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

def index_about(request):
    return render(request,"about.html")