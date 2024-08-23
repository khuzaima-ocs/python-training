from django.contrib import admin
from .models import Book, Library, LibraryBook
from .inlines import LibraryBookInline

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = ('title', 'author', 'publish_date')
    list_display_links = ('title',)
    search_fields = ('title', 'author', 'content')
    inlines = [LibraryBookInline]
    
    
@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):

    list_display = ('name', 'location', 'book_count')
    list_display_links = ('name',)
    search_fields = ('name', 'location')
    inlines = [LibraryBookInline]

    def book_count(self, obj):
        return obj.librarybook_set.count()

    book_count.short_description = 'Books Count'

     
@admin.register(LibraryBook)
class LibraryBookAdmin(admin.ModelAdmin):

    list_display = ('get_library_name', 'get_book_name')
    list_display_links = ('get_library_name', 'get_book_name')
    search_fields = ('get_library_name', 'get_book_name')

    def get_library_name(self, obj):
        return obj.library.name
    get_library_name.short_description = 'Library Name'

    def get_book_name(self, obj):
        return obj.book.title
    get_book_name.short_description = 'Book Title'