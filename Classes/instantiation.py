# 3. Instantiation
#    Create an instance of the Car class and print out its description using the method defined.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def fullname(self):
        return f"This is a {self.make} {self.model} created in {self.year}"


c1 = Car("Toyota", "Hyundai", 2018)
print(c1.fullname())
