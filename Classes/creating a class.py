# 1. Create a `Car` class
#    Define a Car class with attributes for make, model, and year. Include a method to display the full
#    description of the car.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def fullname(self):
        return f"This is a {self.make} {self.model} created in {self.year}"


c1 = Car("Toyota", "Hyundai", 2018)
print(c1.fullname())
