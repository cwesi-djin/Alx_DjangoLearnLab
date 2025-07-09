# Delete the book you created
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Things Fall Apart Because The Center Cannot Hold") 
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>