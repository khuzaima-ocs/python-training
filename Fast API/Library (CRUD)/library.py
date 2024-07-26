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
        book = None
        if title not in self.indices:
            return {
                "message": "No such book in our collection.",
                "data": book
            }

        index = self.indices[title]
        
        with open(self.file_path, 'rb') as f:
            f.seek(Book.SIZE * index)
            data = f.read(Book.SIZE)
            book = Book.unpack(data)

        return {
                "message": "Success",
                "data": book.get_data()
            }
    
    def get_book_obj(self, title):
        book = None
        if title not in self.indices:
            return {
                "message": "No such book in our collection.",
                "book": book
            }

        index = self.indices[title]
        
        with open(self.file_path, 'rb') as f:
            f.seek(Book.SIZE * index)
            data = f.read(Book.SIZE)
            book = Book.unpack(data)

        return {
                "message": "Success",
                "book": book
            }

    def get_book_titles(self):
        books = []
        for book in self.indices:
            books.append(book.capitalize())
        return books

    def edit_book(self, title: str, new_title, new_author, new_content):
        response = self.get_book_obj(title)
        if response['book']:
            index = self.indices[title]
            updated_book = response['book'].edit_book(new_title, new_author, new_content)

            with open(self.file_path, 'r+b') as f:
                f.seek(index * Book.SIZE)
                f.write(updated_book.pack())

            if title.lower() != updated_book.title.rstrip('\0').lower():
                del self.indices[title.lower()]
                self.indices[updated_book.title.rstrip('\0').lower()] = index

            return {
                "message": "Book edited successfully"
            }
        
        else:
            return {
                "message": "Book not found..",
            }

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

            return {
                "message": "Book deleted."
            }

        else:
            return {
                "message": "Book not found.",
            }