from django.urls import path
from . import views

url_patterns = [
    path('books/', views.ListView.as_view()),
    path('books/<int:pk>', views.ListView.as_view, name='book-list'),
    path('books/', views.DetailView.as_view()),
    path('books/<int:pk>', views.DetailView.as_view, name='book-detail'),
    path('books/create/', views.CreateView.as_view()),
    path('books/<int:pk>', views.CreateView.as_view, name='book-create'),
    path('books/update/', views.UpdateView.as_view()),
    path('books/<int:pk>', views.UpdateView.as_view, name='book-update'),
    path('books/delete/', views.DeleteView.as_view()),
    path('books/<int:pk>', views.DeleteView.as_view, name='book-delete'),
]