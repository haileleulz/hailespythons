# 11. Implement magic methods
#     Add the __str__ and __repr__ magic methods to the Car class to customize what gets printed when a Car
#     instance is printed and represented.

class Car:
    def __init__(self, make, model, year, initial_mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.__initial_mileage = initial_mileage

    def __str__(self):
        print(f"This is a {self.make} {self.model} created in {self.year}")

    def __repr__(self):
        print(f"This is a {self.make} {self.model} created in {self.year} with an initial "
              f"millage of {self.__initial_mileage}")


c1 = Car("Toyota", "Hyundai", 2018)
c1.__str__()
c1.__repr__()
