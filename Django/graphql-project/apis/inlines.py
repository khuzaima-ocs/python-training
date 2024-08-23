from django.contrib import admin
from .models import Book, Library, LibraryBook


class LibraryBookInline(admin.TabularInline):
    model = LibraryBook
    extra = 0 
    classes = ("grp-collapse", "grp-open",)
    inline_classes = ("grp-collapse", "grp-closed",)
    show_change_link = True