from person import Person

class Book:
    def __init__(self, title, author, content) -> None:
        self.content = content
        self.author = author
        self.title = title
        self.available = True
        self.borrowers = []
    
    def __str__(self) -> str:
        return f"""
Book Title:     {self.title}
Author:         {self.author}
Content:        {self.content}
"""
    
    def edit_book(self):
        print(f"Editing book:  {self.title}\n")
        
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

        return self

    def print(self):
        print(self)

    def borrow(self, person: Person):
        if self.available:
            self.available = False
            self.borrowers.append(person.id)
            person.borrow(self.title)
        else:
            print("Book already assigned to someone..")
    
    def handle_return(self, person: Person):
        if self.title in person.books:
            self.available = True
            person.handle_return(self.title)

        else:
            print("You don't have this book")