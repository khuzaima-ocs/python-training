import graphene
from graphene_django import DjangoObjectType
from .models import Book, Library, LibraryBook

class BookType(DjangoObjectType):
    class Meta:
        model = Book

class LibraryType(DjangoObjectType):
    class Meta:
        model = Library

class LibraryBookType(DjangoObjectType):
    class Meta:
        model = LibraryBook
    
class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    all_libraries = graphene.List(LibraryType)
    books_by_library = graphene.List(BookType)

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()
    
    def resolve_all_libraries(self, info, **kwargs):
        return Library.objects.all()
    
schema = graphene.Schema(query=Query)