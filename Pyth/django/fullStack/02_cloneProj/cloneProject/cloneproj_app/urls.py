from django.conf.urls import url
from cloneproj_app import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
]