#this page makes crud page show 


from django.forms import ModelForm 
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "featured_image", "description", "demo_link", "tags"]