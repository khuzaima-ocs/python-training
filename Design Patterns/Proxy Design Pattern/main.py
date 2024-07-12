from proxy_book_data import ProxyBookData

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
