from .models import Book, Author
from rest_framework import serializers
import datetime

#Book model serializer converts book instances to JSON
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

#custom validator to ensure the publication_year is not in the future.
    def validation_publication_year(self, value):
        current_year = datetime.now().year

        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be set in the future.")
        return value

#Author model serializer converts author instances to JSON
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name'] 