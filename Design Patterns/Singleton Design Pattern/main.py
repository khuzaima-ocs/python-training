from person import PersonSingleton

if __name__ == "__main__":
    p1 = PersonSingleton("Khuzaima", 23)
    PersonSingleton.print_data()
    p2 = PersonSingleton.get_instance()
    p2.print_data()