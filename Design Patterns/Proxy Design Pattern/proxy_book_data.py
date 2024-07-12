from ibook_data import IBookData
from real_book_data import RealBookData
import datetime

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