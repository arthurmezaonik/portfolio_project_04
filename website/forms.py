from django import forms
from django.forms import ModelForm, fields
from .models import Publication

class PublicationForm(ModelForm):
    class Meta:
        model = Publication
        fields = ('title', 'small_description', 'description', 'contact_email', 'job_type',)
