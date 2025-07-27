from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Book

from django.contrib.auth.decorators import permission_required

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})