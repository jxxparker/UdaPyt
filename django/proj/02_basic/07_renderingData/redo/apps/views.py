from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "apps/index.html")

def project(request, pk):
    return HttpResponse("Single Project " + " " + str(pk))