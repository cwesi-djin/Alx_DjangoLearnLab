# Retrieve and display all attributes of the book
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Things fall apart")
>>> book.title, book.author, book.publication_year
('Things fall apart', 'Chinua Achebe', 1958)