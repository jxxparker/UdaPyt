from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        "id": "1",
        "title": "Eccomerce Website",
        "description": "Fully functional ecomerce website"
    },
    {
        "id": "2",
        "title": "Portfolio Website",
        "description": "This was project where I built out for my portoflio"
    },
    {
        "id": "3",
        "title": "Social Network",
        "description": "Awesome open source projects that is being worked on."
    },
]

def index(request):
    page = "projects"
    msg = "Hello, you are on index page."
    number = 10
    context = {"page" : page, "number" : number, "lists": projectsList}
    return render(request, "apps/index.html", context)

def display(request, pk):
    projectObj = None
    for i in projectsList:
        if i["id"] == pk:
            projectObj = i
    return render(request, "apps/display.html", {"obj": projectObj})