from person_factory import PersonFactory

if __name__ == "__main__":
    choice = input("Are you (Student) or (Teacher)? ")

    person = PersonFactory.build_person(choice)
    if person != -1:
        person.display()