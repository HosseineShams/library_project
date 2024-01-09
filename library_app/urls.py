from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, AuthorViewSet, RegisterUserAPIView

# Creating a router object to handle viewsets automatically.
router = DefaultRouter()

# Registering the BookViewSet with the router.
# This will automatically create URL patterns for CRUD operations on books.
router.register(r'books', BookViewSet)

# Registering the AuthorViewSet with the router.
# This will automatically create URL patterns for CRUD operations on authors.
router.register(r'authors', AuthorViewSet)

# URL patterns for the app.
urlpatterns = [
    # Includes all URL patterns that the router generates.
    path('', include(router.urls)),

    # A dedicated path for user registration.
    # It maps to the RegisterUserAPIView and is named 'register'.
    path('register/', RegisterUserAPIView.as_view(), name='register'),
]
