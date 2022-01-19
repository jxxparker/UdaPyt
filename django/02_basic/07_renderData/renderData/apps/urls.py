from django.urls import path
from apps import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index2/<str:pk>', views.index2, name="index2"), 
    
    
]