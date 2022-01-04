from django import forms
from django.forms import ModelForm
from .models import Publication

class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'author_fname', 'author_lname', 'small_description', 'description', 'contact_email', 'job_type',)
