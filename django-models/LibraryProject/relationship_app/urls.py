from django.urls import path
from .views import list_books, LibraryDetail

urlpattern = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetail.as_view(), name='library_detail'),
]