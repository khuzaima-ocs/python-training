from pathlib import Path
from book import Book
import pickle

class Library: 
    def __init__(self):
        self.path = Path("Books")

        if not self.path.exists():
            self.path.mkdir()

    def add_book(self, book: Book):
        with open(f'./{self.path}/{book.title}.pkl', 'wb') as file:
            pickle.dump(book, file)

    def add_new_book(self, content: str, author: str, title: str):
        book = Book(content, author, title)
        self.add_book(book)

    def get_book(self, title: str):
        book = None
        for book_file in self.path.glob("*.pkl"):
            if title.strip().lower() + '.pkl' == book_file.name.strip().lower():
                with open(book_file, 'rb') as file:
                    book = pickle.load(file)

        return book    
                
    def delete_book(self, title: str):
        for book in self.path.glob("*.pkl"):
            if title.strip().lower() + '.pkl' == book.name.strip().lower():
                book.unlink()
                break

        else:
            print("No such book in our collection.")

    def search_by_content(self, text: str):
        books = []
        for book in self.path.glob("*.pkl"):
            with open(book, 'rb') as file:
                book_data: Book = pickle.load(file)
                content = book_data.content.strip()
                
                if content.lower().__contains__(text.strip().lower()):
                    books.append(book.name[:-4])

        if not len(books):
            print(f"'{text}' is not present in any book..")
        else:
            print(f"'{text}' is present in following books: ")
            for book in books: 
                print(f"- {book}")

    def show_book_titles(self):
        for book in self.path.glob("*.pkl"):
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
      
    def borrow(self, title, person_id):
        book = self.get_book(title)
        if book:
            book.borrow(person_id)
            
            self.delete_book(title)
            self.add_book(book)
        else:
            print("No such book in our collection")

    def handle_return(self, title, person_id):
        book = self.get_book(title)
        if book:
            book.handle_return(person_id)
            self.delete_book(title)
            self.add_book(book)

        else:
            print("No such book in our collection")