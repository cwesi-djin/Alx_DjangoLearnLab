# Update the title of “1984” to “Nineteen Eighty-Four”
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Things fall apart")
>>> book.title = "Things Fall Apart Because The Center Cannot Hold"
>>> book.save()
>>> book.title
'Things Fall Apart Because The Center Cannot Hold'