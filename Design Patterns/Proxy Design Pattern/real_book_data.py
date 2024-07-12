from ibook_data import IBookData

class RealBookData(IBookData):

    def __init__(self) -> None:
        self.books = [
            {"id": 1,"title": "1984", "author": "George Orwell", "year": 1949},
            {"id": 2,"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
            {"id": 3,"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
        ]

    def get_book_info(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                return book
            
        print("Book not found..!")