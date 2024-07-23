from pathlib import Path
from book import Book

class Library:

    def __init__(self):
        self.file_path = Path("library.bin")
        self.indices = {}
        self.__load_indices()

    def __load_indices(self):
        if self.file_path.exists():
            with open(self.file_path, 'rb') as f:
                index = 0
                while True:
                    data = f.read(Book.SIZE)
                    if len(data) < Book.SIZE:
                        break
                    book = Book.unpack(data)
                    self.indices[book.title.rstrip('\0').lower()] = index
                    index += 1

    def __add_book(self, book: Book):
        with open(self.file_path, 'ab') as f:
            f.write(book.pack())

        self.indices[book.title.rstrip('\0').lower()] = len(self.indices)

    def add_new_book(self, title: str, author: str, content: str):
        if title.lower() in self.indices:
            print("Book already present in library")
            return
        book = Book(title, author, content)
        self.__add_book(book)
    
    def get_book(self, title):
        if title not in self.indices:
            print("No such book in our collection.")
            return
        
        index = self.indices[title]
        with open(self.file_path, 'rb') as f:
            f.seek(Book.SIZE * index)
            data = f.read(Book.SIZE)
            return Book.unpack(data)
        
    def show_book_titles(self):
        if not len(self.indices):
            print("No book in the library")
        
        for book in self.indices:
            print(f" - {book.capitalize()}")
            
    def print_book(self, title: str):
        book = self.get_book(title)
        if book:
            print(book)

    def edit_book(self, title: str, borrower: str, is_returning = False):
        book = self.get_book(title)
        if book:
            index = self.indices[title]
            updated_book = None
            if borrower == "":
                updated_book = book.edit_book()

            elif not is_returning:
                book.borrow(borrower)
                updated_book = book

            else:
                book.handle_return(borrower)
                updated_book = book

            with open(self.file_path, 'r+b') as f:
                f.seek(index * Book.SIZE)
                f.write(updated_book.pack())
        
            if title.lower() != updated_book.title.rstrip('\0').lower():
                del self.indices[title.lower()]
                self.indices[updated_book.title.rstrip('\0').lower()] = index

    def delete_book(self, title: str):
        if title.lower() in self.indices:
            index_to_delete = self.indices[title.lower()]
            last_index = len(self.indices) - 1

            if index_to_delete != last_index:
                last_book_title = ""
                for book, index in self.indices.items():
                    if index == last_index:
                        last_book_title = book

                with open(self.file_path, 'r+b') as f:
                    f.seek(last_index * Book.SIZE)
                    last_book_data = f.read(Book.SIZE)
                    
                    f.seek(index_to_delete * Book.SIZE)
                    f.write(last_book_data)
        
                self.indices[last_book_title] = index_to_delete
        
            del self.indices[title.lower()]
        
            with open(self.file_path, 'r+b') as f:
                f.truncate(len(self.indices) * Book.SIZE)

            print("Deleted Successfully.")
        
        else:
            print("No such book in our collection.")
            