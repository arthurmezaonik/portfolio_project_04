from django.shortcuts import render
from .models import Publication


def index(request):
    return render(request, 'index.html', {})


def worker_publication(request):
    publications = Publication.objects.all()
    return render(request, 'publications.html', {
        'publications': publications,
    })
