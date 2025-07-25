from app1.models import Book, Author
from rest_framework import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Author
        fields = ['name', 'surname', 'books']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title']

