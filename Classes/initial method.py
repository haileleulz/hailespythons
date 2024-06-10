# 2. Add an initialization method
#    Modify the Car class to include an __init__ method that initializes the make, model, and year attributes.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def fullname(self):
        return f"This is a {self.make} {self.model} created in {self.year}"
