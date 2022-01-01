from django.db import models
from django.db.models import F
from django.contrib.auth.models import User

WORK_TYPES = (
    (0, 'Plumber'),
    (1, 'Electrical'),
    (2, 'Small Repairs'),
    (3, 'Flooring'),
    (4, 'Painting'),
    (5, 'Cleaner'),
    (6, 'Other'),
)


class Publication(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="job_author"
    )
    small_description = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact_email = models.EmailField(max_length=254)
    job_type = models.IntegerField(choices=WORK_TYPES)
    likes = models.ManyToManyField(
        User, related_name='job_like', blank=True
    )

    class Meta:
        ordering = [F('author').asc(nulls_last=True)]

    def __str__(self):
        return f'{self.title} created by {self.author}'

    def number_of_likes(self):
        return self.likes.count()


class Review(models.Model):
    job = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.review} by {self.name}"
