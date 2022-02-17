from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "apps/index.html")

def aboutme(request):
    return render(request, "apps/aboutme.html")

def contactme(request):
    return render(request, "apps/contactme.html")

def projects(request):
    return render(request, "apps/projects.html")


