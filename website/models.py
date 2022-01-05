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
    """
        This model represents how the publication is created.
        It's associated to the user that created the publication via author_id.
    """
    title = models.CharField(max_length=200, unique=True)
    author_fname = models.CharField('First Name', max_length=200,)
    author_lname = models.CharField('Last Name', max_length=200,)
    author_id = models.IntegerField('Author ID', default=1)
    small_description = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact_email = models.EmailField(max_length=254)
    job_type = models.IntegerField(choices=WORK_TYPES)
    likes = models.ManyToManyField(
        User, related_name='job_like', blank=True
    )

    class Meta:
        ordering = [F('author_fname').asc(nulls_last=True)]

    def __str__(self):
        """ model that returns publication title and author name """
        return f'{self.title} created by {self.author_fname}'

    def number_of_likes(self):
        """ model that returns likes on the publication """
        return self.likes.count()


class Review(models.Model):
    """This model represents how the reviews are created"""
    publication = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="reviews")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    review = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        """ model that returns the review content and author name """
        return f"Comment {self.review} by {self.name}"
