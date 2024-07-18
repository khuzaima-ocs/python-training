
class Person:

    def __init__(self, id, name) -> None:
        self.id = id
        self.name = name
        self.books = []

    def borrow(self, bookTitle):
        self.books.append(bookTitle)

    def handle_return(self, bookTitle):
        self.books = list(filter(lambda title: title != bookTitle, self.books))