from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    google_books_id = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    categories = models.CharField(max_length=200)
    cover_url = models.URLField()


