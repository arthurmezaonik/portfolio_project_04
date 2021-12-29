from django.urls import path
from .views import index, worker_publication

urlpatterns = [
    path('', index, name='index'),
    path('publications/', worker_publication, name='worker_publication'),
]
