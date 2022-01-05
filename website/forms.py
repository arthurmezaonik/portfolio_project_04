from django import forms
from django.forms import ModelForm, widgets
from .models import Publication

class PublicationForm(ModelForm):
    """Form to create a new publication"""
    class Meta:
        model = Publication
        fields = (
            'title',
            'author_fname',
            'author_lname',
            'small_description',
            'description',
            'contact_email',
            'job_type',
            )

        labels = {
            'title' : '',
            'author_fname' : '',
            'author_lname' : '',
            'small_description' : '',
            'description' : '',
            'contact_email' : '',
        }

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title*',}),
            'author_fname' : forms.TextInput(attrs={
                'class':'form-control', 'placeholder':'First Name*',
            }),
            'author_lname' : forms.TextInput(attrs={
                'class':'form-control', 'placeholder':'Last Name*',
            }),
            'small_description' : forms.TextInput(attrs={
                'class':'form-control', 'placeholder':'Small Description',
            }),
            'description' : forms.Textarea(attrs={
                'class':'form-control', 'placeholder':'Description',
            }),
            'contact_email' : forms.EmailInput(attrs={
                'class':'form-control', 'placeholder':'Contact Email*',
            }),
        }
