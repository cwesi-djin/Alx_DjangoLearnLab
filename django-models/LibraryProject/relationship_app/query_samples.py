
import os
import django

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return author.books.all()

# 2. List all books in a specific library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# 3. Retrieve the librarian for a library
def librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian

# Sample usage (after populating database via admin or shell)
if __name__ == "__main__":
    print("Books by Author 'Chinua Achebe':")
    for book in books_by_author('Chinua Achebe'):
        print("-", book.title)

    print("\nBooks in 'Central Library':")
    for book in books_in_library('Central Library'):
        print("-", book.title)

    print("\nLibrarian of 'Central Library':")
    print(librarian_for_library('Central Library').name)