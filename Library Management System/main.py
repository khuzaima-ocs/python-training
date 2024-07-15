class Book:

    def __init__(self, content, author, title) -> None:
        self.content = content
        self.author = author
        self.title = title
    
    def __str__(self) -> str:
        return f"""
Book Title:     {self.title}
Author:         {self.author}
Content:        {self.content}
"""
    
    def edit_book(self):
        print(f"Editing book {self.title}\n")
        
        print(f"Title ({self.title}) : ", end="")
        new_title = input()

        print(f"Author ({self.author}) : ", end="")
        new_author = input()

        print(f"Content ({self.content[:24]}) : ", end="")
        new_content = input()

        if new_title and new_title.strip() != "":
            self.title = new_title

        if new_author and new_author.strip() != "":
            self.author = new_author

        if new_content and new_content.strip() != "":
            self.content = new_content

        print(self)
    
class Library:
    
    def __init__(self):
        self.books: list[Book] = []

        
    def add_book(self, content, author, title):
        book = Book(content, author, title)
        self.books.append(book)

    def get_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
            

    def delete_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)

    def show_book_titles(self):
        for book in self.books:
            print(f" - {book.title}")

    def print_book(self, title: str):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(book)
    

lib = Library()

lib.add_book("Hello WOrld", "Khuzaima", "C++")
lib.add_book("Learn Python", "Mosh", "Fluent Python")

book: Book = lib.get_book("c++")