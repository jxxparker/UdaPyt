from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Projects page worked.")
    return render(request, "apps/index.html")

def index2(request, pk):
    # return HttpResponse("this page will work with whatever word after THIS" + " " + str(pk))
    return render(request, "apps/index2.html")




