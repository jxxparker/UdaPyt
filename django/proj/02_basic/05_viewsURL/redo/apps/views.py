from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Index Page")

def project(request, pk):
    return HttpResponse("Single Project " + " " + str(pk))