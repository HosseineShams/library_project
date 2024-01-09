from django.test import TestCase
from django.contrib.auth.models import User
from .models import Author, Book
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from datetime import date

# Model Tests

class AuthorModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='12345')
        Author.objects.create(name='John Doe', birth_date=date.today(), bio='Test Bio', user=test_user)

    def test_name_label(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    

class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_author = Author.objects.create(name='John Doe', birth_date=date.today(), bio='Test Bio', user=test_user)
        test_book = Book.objects.create(title='Test Book', genre='Fiction', publication_date=date.today(), availability_status=True, user=test_user)
        test_book.authors.add(test_author)

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'title')

   

# View Tests

class AuthorViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        Author.objects.create(name='John Doe', birth_date=date.today(), bio='Test Bio', user=self.user)

    def test_create_author(self):
        url = reverse('author-list')
        data = {"name": "Jane Doe", "birth_date": "1990-01-01", "bio": "Another Test Bio"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_author(self):
        author = Author.objects.get(name='John Doe')
        url = reverse('author-detail', args=[author.id])
        data = {
            "name": "Updated Author Name",
            "birth_date": "1990-01-01",  # Ensure the format is correct
            "bio": "Updated Test Bio"
        }
        response = self.client.put(url, data, format='json')
        if response.status_code != status.HTTP_200_OK:
            print(response.data)  # Debugging line
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_author(self):
        author = Author.objects.get(name='John Doe')
        url = reverse('author-detail', args=[author.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class BookViewSetTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.author = Author.objects.create(name='John Doe', birth_date=date.today(), bio='Test Bio', user=self.user)
        self.book = Book.objects.create(title='Test Book', genre='Fiction', publication_date=date.today(), availability_status=True, user=self.user)
        self.book.authors.add(self.author)

    def test_create_book(self):
        url = reverse('book-list')
        data = {"title": "New Book", "genre": "Non-Fiction", "publication_date": "2022-01-01", "availability_status": True, "authors": [self.author.id]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book.id])
        data = {
            "title": "Updated Book",
            "genre": "Non-Fiction",
            "publication_date": "2022-01-01",  # Ensure the format is correct
            "availability_status": False,
            "authors": [self.author.id]  # Ensure author ID is correct
        }
        response = self.client.put(url, data, format='json')
        if response.status_code != status.HTTP_200_OK:
            print(response.data)  # Debugging line
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
