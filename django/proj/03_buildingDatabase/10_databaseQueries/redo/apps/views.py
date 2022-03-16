from django.shortcuts import render
from django.http import HttpResponse
from .models import Project

def index(request):
    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "apps/index.html", context)

def display(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, "apps/display.html", {"projectObj": projectObj})