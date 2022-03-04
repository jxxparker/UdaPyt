from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def index(request):
    projects = Project.objects.all()
    context = {"lists": projects}
    return render(request, "apps/index.html", context)

def display(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, "apps/display.html", {"projectObj": projectObj})

def create(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form": form}
    return render(request, "apps/crud.html", context)
    
