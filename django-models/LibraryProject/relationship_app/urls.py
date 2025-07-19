from django.urls import path
from .views import list_books, LibraryDetailView, login_view, logout_view, list_books, register_view

urlpattern = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),


    #Athentication URL's
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]