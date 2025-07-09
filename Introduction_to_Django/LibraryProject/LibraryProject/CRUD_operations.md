# create.md
from bookshelf.models import Book
book = Book.objects.create(title="Things fall apart", author="Chinua Achebe", publication_year=1958)
book
<Book: Things fall apart>

# retrieve.md
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Things fall apart")
>>> book.title, book.author, book.publication_year
('Things fall apart', 'Chinua Achebe', 1958)

# update.md
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Things fall apart")
>>> book.title = "Things Fall Apart Because The Center Cannot Hold"
>>> book.save()
>>> book.title
'Things Fall Apart Because The Center Cannot Hold'

# delete.md
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Things Fall Apart Because The Center Cannot Hold") 
>>> book.delete()
(1, {'bookshelf.Book': 1})
>>> Book.objects.all()
<QuerySet []>