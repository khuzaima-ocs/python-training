
class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f"Hello, I am {self.name} & I am {self.age} years old."
    
    def celebrate_birthday(self) -> None:
        self.age += 1
        print(f"Happy birthday to you 🎉. You have turned {self.age} today")
        

class Employee(Person):
    def __init__(self, name, age, salary, profession) -> None:
        super().__init__(name, age)
        self.salary = salary
        self.profession = profession

    # Overridden function
    def __str__(self) -> str:
        text = super().__str__()
        text += ' '
        text += f"I am {self.profession} & my salary is {self.salary}/month. "
        return text
    

class Programmer(Employee):
    def __init__(self, name, age, salary, profession, stack, company) -> None:
        super().__init__(name, age, salary, profession)
        self.stack = stack
        self.company = company
    
    def __str__(self) -> str:
        text = super().__str__()
        text += ' '
        text += f"My tech stack is {self.stack} & I am working at {self.company}"
        return text

p1 = Programmer("Khuzaima", 23, 50000, "ASE", "MERN", "OClooud Solutions")
print(p1)
p1.celebrate_birthday()
print(p1)
