# Python program to implement parameterized constructor
class Syam:
    def __init__(self, name, roll, address):
      
        self.name = name
        self.roll = roll
        self.address = address

car = Syam("Chinni", 2022,"benguluru")
print(car.name)
print(car.roll)
print(car.address)
