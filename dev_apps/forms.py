from dataclasses import field
from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'feature_image', 'description', 'demo_link', 'source_link', 'tags']