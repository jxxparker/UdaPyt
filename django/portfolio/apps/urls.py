from django.urls import path
from apps import views

urlpatterns = [
    path('', views.index, name="index"),
    path('aboutme/', views.aboutme, name="aboutme"),
    path('contactme/', views.contactme, name="contactme"),
    path('projects/', views.projects, name="projects"),

]