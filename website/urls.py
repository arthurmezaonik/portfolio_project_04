from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('publications/', views.worker_publication, name='worker_publication'),
    path(
        'create_publications/',
        views.create_publications,
        name='create_publications'
    ),
    path('user_area/<user_id>', views.user_area, name='user_area'),
    path(
        'publication_detail/<publication_id>',
        views.publication_detail,
        name='publication_detail'
    ),
    path(
        'update_publication/<publication_id>',
        views.update_publication,
        name='update_publication'
    ),
    path(
        'delete_publication/<publication_id>',
        views.delete_publication,
        name='delete_publication'
    ),
    path('search/', views.search, name='search'),
]
