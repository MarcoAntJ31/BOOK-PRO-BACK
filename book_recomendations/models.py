from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    google_books_id = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    categories = models.CharField(max_length=200)
    cover_url = models.URLField()

class UserRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField() 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_categories = models.CharField(max_length=200)  
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    profile_picture = models.URLField()
    
    def __str__(self):
        return self.user.username
