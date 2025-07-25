from rest_framework import viewsets
from app1.models import Book, Author
from app1.serializers import BookSerializer, AuthorSerializer

# Create your views here.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer