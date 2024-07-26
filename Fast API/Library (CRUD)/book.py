import struct

class Book:
    FORMAT = '32s32s1000s32s'
    SIZE = struct.calcsize(FORMAT)

    def __init__(self, title, author, content):
        self.title = title[:31].ljust(32, '\0')
        self.author = author[:31].ljust(32, '\0')
        self.content = content[:999].ljust(1000, '\0')
        self.borrower = "".ljust(32, '\0')

    def get_data(self):
        return {
            "title": self.title.strip('\0'),
            "author": self.author.strip('\0'),
            "content": self.content.strip('\0'),
            "borrower": self.borrower.strip('\0') or None
        }
       
    def pack(self):
        return struct.pack(self.FORMAT, self.title.encode(), self.author.encode(), self.content.encode(), self.borrower.encode())

    @classmethod
    def unpack(cls, data):
        title, author, content, borrower = struct.unpack(cls.FORMAT, data)
        book = cls(title.decode('utf-8').rstrip('\0'), 
                   author.decode('utf-8').rstrip('\0'), 
                   content.decode('utf-8').rstrip('\0'))
        book.borrower = borrower.decode('utf-8').rstrip('\0') or ""
        return book

    def edit_book(self, new_title, new_author, new_content):
        if new_title and new_title.strip() != "":
            self.title = new_title

        if new_author and new_author.strip() != "":
            self.author = new_author

        if new_content and new_content.strip() != "":
            self.content = new_content

        return self

    def borrow(self, person):
        if not len(self.borrower.strip('\0')):
            self.borrower = person
        else:
            print("Book not available at this very moment.")

    def handle_return(self, borrower: str):
        if self.borrower.lower() == borrower.lower():
            self.borrower = ""
        else:
            print("You don't have this book.")