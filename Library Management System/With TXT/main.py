from library import Library
from person import Person

if __name__ == "__main__":      
    library = Library()

    print("""***** WELCOME TO LIBRARY MANAGEMENT SYSTEM *****""")

    guide = """
1: Add
2: Read
3: Delete
4: Edit
5: Search
6: Show Titles
7: Show Count
8: Print Guide
9: Quit"""

    print(guide)
    while True:
        isValidInput = False
        while not isValidInput:
            try:
                inp = int(input("\nEnter your choice: "))
                isValidInput = True
            except Exception as e:
                print("Invalid Input..")

        match inp:
            case 1:
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                content = input("Enter book content: ")
                library.add_new_book(title.strip(), author.strip(), content.strip())

            case 2:
                title = input("Enter title of the book you want to read: ")
                library.print_book(title)

            case 3:
                title = input("Enter title of the book you want to delete: ")
                library.delete_book(title)

            case 4:
                title = input("Enter title of the book you want to edit: ")
                library.edit_book(title)

            case 5:
                text = input("Enter search text: ")
                library.search_by_content(text)


            case 6:
                library.show_book_titles()

            case 7:
                library.book_count()

            case 8:
                print(guide)

            case 9:
                print("Thank you..\n")
                break
                
            case _:
                print("Invalid input..")