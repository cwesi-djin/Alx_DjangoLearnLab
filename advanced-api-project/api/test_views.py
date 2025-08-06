from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user and authenticate
        self.user = User.objects.create_user(username='tester', password='testpass')
        self.client.login(username='tester', password='testpass')

        # Create author and books
        self.author = Author.objects.create(name="Chinua Achebe")
        self.book = Book.objects.create(
            title="Things Fall Apart",
            publication_year=1958,
            author=self.author
        )

    def test_create_book(self):
        url = reverse('book-create')
        data = {
            "title": "No Longer at Ease",
            "publication_year": 1960,
            "author": self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "No Longer at Ease")

    def test_get_book_detail(self):
        url = reverse('book-detail', args=[self.book.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Things Fall Apart")

    def test_update_book(self):
        url = reverse('book-update', args=[self.book.id])
        data = {
            "title": "Things Fall Apart (Updated)",
            "publication_year": 1958,
            "author": self.author.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Things Fall Apart (Updated)")

    def test_delete_book(self):
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_filter_books_by_year(self):
        url = reverse('book-list-create') + '?publication_year=1958'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_by_title(self):
        url = reverse('book-list-create') + '?search=Things'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_permission_required_for_create(self):
        self.client.logout()
        url = reverse('book-create')
        data = {
            "title": "The River Between",
            "publication_year": 1965,
            "author": self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
