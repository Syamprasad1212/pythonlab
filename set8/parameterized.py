class Person:
    def __init__(self, name, age):
        self.name = name  # Initialize name attribute
        self.age = age    # Initialize age attribute

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating object with parameters
p1 = Person("Alice", 25)
p1.display()
