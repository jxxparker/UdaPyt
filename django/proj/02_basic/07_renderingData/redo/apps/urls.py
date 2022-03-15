from django.urls import path, include
from apps import views

urlpatterns =[
    path("index/", views.index, name="index"),
    path("display/<str:pk>", views.display, name="display")
]