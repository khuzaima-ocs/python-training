class PersonSingleton:

    __instance = None

    def __init__(self, name, age) -> None:
        if PersonSingleton.__instance != None:
            raise Exception("Person object has already been created..!!")
        
        self.name = name
        self.age = age
        PersonSingleton.__instance = self

    @staticmethod
    def get_instance():
        if PersonSingleton.__instance == None:
            PersonSingleton("N/A", 0)

        return PersonSingleton.__instance
    
    @staticmethod
    def print_data():
        print(f"Name: {PersonSingleton.__instance.name}, Age: {PersonSingleton.__instance.age}")