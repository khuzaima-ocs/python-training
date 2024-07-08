from abc import ABCMeta, abstractmethod

class IPerson(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def display():
        pass
    

class Student(IPerson):
    def display(self):
        print("I am Student")

class Teacher(IPerson):
    def display(self):
        print("I am Teacher")

class PersonFactory:
    
    @staticmethod
    def build_person(choice):
        if choice == "Student":
            return Student()

        if choice == "Teacher":
            return Teacher()
        print("Invalid Input")
        return -1

if __name__ == "__main__":
    choice = input("Are you (Student) or (Teacher)? ")

    person = PersonFactory.build_person(choice)
    if person != -1:
        person.display()
    

