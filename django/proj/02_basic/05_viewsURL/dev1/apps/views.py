from django.shortcuts import render
from django.http import HttpResponse

def projects(request):
    return HttpResponse("Our products")

def project(request, pk):
    return HttpResponse("Single Project " + " " + str(pk))