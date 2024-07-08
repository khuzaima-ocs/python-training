class Person:
    __count = 0
    def __init__(self, name, age) -> None:

        # Private members start with "__"
        self.__name = name
        self.__age = age
        Person.__count += 1

    # With this annotation, this function has become a getter
    @property
    def Name(self): 
        return self.__name
    
    # This is setter now. Python don't allow function overloading,
    # but with this annotation, it allows us to and becomes setter.
    @Name.setter
    def Name(self, name):
        self.__name = name

    @staticmethod
    def get_count():
        return Person.__count

p = Person("Khuzaima", 23)
print(p.Name)
p.Name = "Adeel"
print(p.Name)
print(Person.get_count())