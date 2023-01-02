from django.contrib import admin
from .models import Publication, Review

# Register your models here.
@admin.register(Publication)
class JWorkerAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_fname', 'author_lname', 'job_type')
    search_fields = ['title', 'description']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'review', 'publication', 'created_on']
    list_filter = ['created_on']
    search_fields = ('name', 'email', 'review')
