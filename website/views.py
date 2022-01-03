from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Publication


def index(request):
    return render(request, 'index.html', {})


def worker_publication(request):
    publications = Publication.objects.all()
    return render(request, 'publications.html', {
        'publications': publications,
    })


def create_publications(request):
    return render(request, 'create_publications.html', {})


def user_area(request, user_id):
    user = User.objects.get(pk=user_id)
    user_publication = Publication.objects.filter(author = user)
    return render(request, 'user_area.html', {
        'user_publication':user_publication,
    })

def publication_detail(request, publication_id):
    publication_list = Publication.objects.filter(pk = publication_id)
    return render (request, 'publication_detail.html', {
        'publication_list':publication_list,
    })
