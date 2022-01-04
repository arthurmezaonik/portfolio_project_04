from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .models import Publication
from .forms import PublicationForm


def index(request):
    return render(request, 'index.html', {})


def worker_publication(request):
    publications = Publication.objects.all()
    return render(request, 'publications.html', {
        'publications': publications,
    })


def create_publications(request):
    submitted = False
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.author_id = request.user.id
            publication.save()
            return HttpResponseRedirect('/create_publications?submitted=True')
    else:
        form = PublicationForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'create_publications.html', {'form':form, 'submitted':submitted})


def user_area(request, user_id):
    user_publication = Publication.objects.filter(author_id = user_id)
    return render(request, 'user_area.html', {
        'user_publication':user_publication,
    })

def publication_detail(request, publication_id):
    publication_list = Publication.objects.filter(pk = publication_id)
    return render (request, 'publication_detail.html', {
        'publication_list':publication_list,
    })
