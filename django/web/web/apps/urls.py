from django.urls import path, include
from apps import views

urlpatterns = [
    path("", views.index, name="index"),
    path('contactme/', views.contactme, name="contactme"),
    path('aboutme/', views.aboutme, name="aboutme"),
    path('projects/', views.projects, name="projects"),
]
