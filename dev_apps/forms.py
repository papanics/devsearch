from dataclasses import field
from django.forms import ModelForm
from django import forms
from .models import Project, Review

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'feature_image', 'description', 'demo_link', 'source_link', 'tags']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs) #overide the class attribute of the fields

        #looping all fields to apply the class input style or attributes
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


        #instead of doing this one by one we gonna loop this instead.
       # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder': 'Add title'})# changing class into input style

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']

        labels = {
            'value': 'Place your vote',
            'body': 'Add a comment with your vote'
        }


    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs) #overide the class attribute of the fields

        #looping all fields to apply the class input style or attributes
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})