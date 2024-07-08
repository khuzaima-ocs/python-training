from abc import ABCMeta, abstractmethod
import datetime

class IBookData(metaclass = ABCMeta):

    @staticmethod
    @abstractmethod
    def get_book_info():
        pass

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

    
class ProxyBookData(IBookData):
    __logs = []
    def __init__(self) -> None:
        self.real_book_data = RealBookData()
        
    # Private
    def __add_to_logs(self, book_id):
        timestamp = datetime.datetime.now().isoformat()
        ProxyBookData.__logs.append(f"Book id {book_id} was accessed at {timestamp}")
    
    def get_book_info(self, book_id):
        self.__add_to_logs(book_id)
        return self.real_book_data.get_book_info(book_id)
    
    @staticmethod
    def print_logs():
        print(ProxyBookData.__logs)



if __name__ == "__main__":
    book = ProxyBookData()

    print("""
1: Get Book Info
2: Print Logs
3: Quit""")
    
    while True:
        choice = int(input("\nEnter choice: "))
        
        if choice == 3:
            break

        if choice == 2:
            ProxyBookData.print_logs()

        if choice == 1:
            id = int(input("Enter book id: "))
            info = book.get_book_info(id)
            print(info)
