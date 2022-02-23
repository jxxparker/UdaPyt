from django.urls import path, include
from apps import views

urlpatterns = [
    path("index/", views.index, name="index"),
    path("project/<str:pk>", views.project, name="project")
]