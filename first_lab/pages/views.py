from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "home.html")

def index_about(request):
    return render(request,"about.html")
