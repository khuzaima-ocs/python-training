from student import Student
from teacher import Teacher

class PersonFactory:
    @staticmethod
    def build_person(choice):
        if choice == "Student":
            return Student()

        if choice == "Teacher":
            return Teacher()
        print("Invalid Input")
        return -1