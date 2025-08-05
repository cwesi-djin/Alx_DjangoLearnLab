from django.db import models

# Create your models here.
# Represents an author in the system
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Represents a Book in the system
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books" ,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"