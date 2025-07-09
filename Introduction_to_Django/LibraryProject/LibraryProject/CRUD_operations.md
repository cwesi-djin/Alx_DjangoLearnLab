# create.md
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
book
<Book: 1984>

# retrieve.md
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title, book.author, book.publication_year
('1984', 'George Orwell', 1949)

# update.md
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book.title
'Nineteen Eighty-Four'

# delete.md
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four") 
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>