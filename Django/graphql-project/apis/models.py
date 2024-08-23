from django.db import models
from django.core.validators import (MinValueValidator)


# Create your models here.
class Book(models.Model):

    title = models.CharField(max_length=100, unique=True, null=False)
    content = models.TextField()
    author = models.CharField(max_length=100)
    publish_date = models.DateField(verbose_name="Publish Date")

    def __str__(self) -> str:
        return f"{self.title}"
    
    
class Library(models.Model):

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Libraries"

    def __str__(self) -> str:
        return f"{self.name}"

    
class LibraryBook(models.Model):

    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book} - {self.library}"
