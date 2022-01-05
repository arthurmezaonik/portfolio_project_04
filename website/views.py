from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.contrib.messages import success
from .models import Publication
from .forms import PublicationForm


def index(request):
    """ Return index page"""
    return render(request, 'index.html', {})


def worker_publication(request):
    """Return all the created publications"""
    publications = Publication.objects.all()
    return render(request, 'publications.html', {
        'publications': publications,
    })


def create_publications(request):
    """Create a new publication"""
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
    """Return a user area with all the user's publications"""
    user_publication = Publication.objects.filter(author_id = user_id)
    return render(request, 'user_area.html', {
        'user_publication':user_publication,
    })

def publication_detail(request, publication_id):
    """Return all the details from a publication"""
    publication = Publication.objects.get(pk = publication_id)
    return render (request, 'publication_detail.html', {
        'publication':publication,
    })

def update_publication(request, publication_id):
    """Update selected publication"""
    publication = Publication.objects.get(pk = publication_id)
    form = PublicationForm(request.POST or None, instance=publication)

    if request.user.id == publication.author_id:
        if form.is_valid():
            form.save()
            success(request,('Your publication was edited!'))
            return redirect('index')
        else:
            success(request,('You are not allowed to edit this publication.'))
            return redirect('index')

    return render(request, 'update_publication.html',{
        'publication':publication,
        'form':form,
    })

def delete_publication(request, publication_id):
    """Delete selected publication"""
    publication = Publication.objects.get(pk = publication_id)
    if request.user.id == publication.author_id:
        publication.delete()
        success(request,('Your publication was deleted!'))
        return redirect('index')
    else:
        success(request,('You are not allowed to delete this publication.'))
        return redirect('index')

def search(request):
    """Return searched publications"""
    if request.method == "POST":
        searched = request.POST['searched']
        publications = Publication.objects.filter(title__icontains=searched)
        return render(request, 'search.html', {'searched':searched, 'publications':publications})
    else:
        return render(request, 'search.html', {})
