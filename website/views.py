from django.shortcuts import render
from .models import Worker


def index(request):
    return render(request, 'index.html', {})


def worker_publication(request):
    publications = Worker.objects.all()
    return render(request, 'publications.html', {
        'publications': publications,
    })
