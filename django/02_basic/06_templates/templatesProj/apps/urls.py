from django.urls import path
from apps import views

urlpatterns = [
    path('index/', views.index, name="projects"),
    path('index2/<str:pk>', views.index2, name="product"), 
    path('main/', views.main, name="main"),
]