from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from .forms import BookSearchForm
from .forms import ExampleForm


# Create your views here.

def book_search(request):
    query = request.GET.get('q', '')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

def book_search(request):
    form = BookSearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['q']
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.none()
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})

def example_form_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # define this route or use another
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})