import sqlite3 as db

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        self.connection = db.connect("my_db.db")
        self.cursor = self.connection.cursor()

    def insert_data(self):
        self.cursor.execute(f"""
            INSERT INTO persons VALUES
            ("{self.name}", {self.age}, "{self.city}")
        """)

        self.connection.commit()

    def load_data(self):
        self.cursor.execute("""
            SELECT * FROM persons
        """)

        result = self.cursor.fetchall()
        print(result)

p1 = Person("Adeel", 23, "Okara")
# p1.insert_data()
p1.load_data()