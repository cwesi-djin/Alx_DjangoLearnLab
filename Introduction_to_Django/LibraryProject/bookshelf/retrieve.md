# Retrieve and display all attributes of the book
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book.title
'Nineteen Eighty-Four'