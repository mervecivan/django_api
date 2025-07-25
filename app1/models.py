from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Author(models.Model):
    name= models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='authors')

    def __str__(self):
        return '%s %s'%(self.name, self.surname)