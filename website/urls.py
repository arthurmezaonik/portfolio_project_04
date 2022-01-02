from django.urls import path
from .views import index, worker_publication, create_publications, user_area

urlpatterns = [
    path('', index, name='index'),
    path('publications/', worker_publication, name='worker_publication'),
    path('create_publications', create_publications, name='create_publications'),
    path('user_area/<user_id>', user_area, name='user_area'),
]
