from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import strftime, localtime

def index(request):
    return render(request, "apps/index.html")





def clear(request):
    print("--SESSION CLEARED!--")
    request.session.clear()
    return redirect('/')