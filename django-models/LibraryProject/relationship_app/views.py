from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library

# Create your views here.
def list_books(request):
    books = Book.object.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetail(DetailView):
    model = Library
    template = 'library_detail.html'
    context_name = 'library'