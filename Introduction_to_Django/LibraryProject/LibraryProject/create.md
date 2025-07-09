# Create a Book instance
>>>from bookshelf.models import Book
>>>book = Book.objects.create(title="Things fall apart", author="Chinua Achebe", publication_year=1958)
>>>book
<Book: Things fall apart>