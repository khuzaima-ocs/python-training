from pathlib import Path
from book import Book

class Library: 
    def __init__(self):
        self.path = Path("Books")

        if not self.path.exists():
            self.path.mkdir()

    def add_book(self, book: Book):
        with open(f'./{self.path}/{book.title}.txt', 'w+') as f:
            f.writelines(
f"""Book Title:     {book.title}
Author:         {book.author}
Content:        {book.content}"""
)

    def add_new_book(self, content: str, author: str, title: str):
        book = Book(content, author, title)
        self.add_book(book)

    def get_book(self, title: str):
        book = None
        for book_file in self.path.glob("*.txt"):
            if title.strip().lower() + '.txt' == book_file.name.strip().lower():
                with open(book_file, 'r') as f:
                    book_title = f.readline()[11:].strip()
                    book_author = f.readline()[7:].strip()
                    book_content = f.readline()[8:].strip()
                    book = Book(book_title, book_author, book_content)

        return book    
                
    def delete_book(self, title: str):
        for book in self.path.glob("*.txt"):
            if title.strip().lower() + '.txt' == book.name.strip().lower():
                book.unlink()
                break

        else:
            print("No such book in our collection.")

    def search_by_content(self, text: str):
        books = []
        for book in self.path.glob("*.txt"):
            with open(book, 'r') as f:
                lines = f.readlines()
                content = lines[2][8:].strip()

                if content.lower().__contains__(text.strip().lower()):
                    books.append(book.name[:-4])

        if not len(books):
            print(f"'{text}' is not present in any book..")
        else:
            print(f"'{text}' is present in following books: ")
            for book in books: 
                print(f"- {book}")

    def show_book_titles(self):
        for book in self.path.glob("*.txt"):
            print(f" - {book.name[:-4]}")

    def print_book(self, title: str):
        book = self.get_book(title)
        if book:
            print(book)
        else:
            print("No such book in our collection.")
    
    def edit_book(self, title: str):
        book = self.get_book(title)
        if book:
            updated_book = book.edit_book()
            self.delete_book(title)
            self.add_book(updated_book)
        else:
            print("No such book in our collection")
      
    def book_count(self):
        print(len(list(self.path.glob("*.txt"))))