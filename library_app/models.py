from django.db import models
from django.conf import settings

class Author(models.Model):
    """
    Model representing an author. Each author has personal details and is linked to a user.
    """
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    bio = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Link to the User model; nullable to allow flexibility.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

class Book(models.Model):
    """
    Model representing a book with details such as title, genre, publication date.
    Tracks the availability status in the library and links to the user who added the book.
    """
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    availability_status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    authors = models.ManyToManyField(Author)
    
    # User association; nullable to denote the user who added the book.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
