# 9. Add private attributes
#    Modify the Car class by adding a private attribute to keep track of the mileage and a public method to
#    update this mileage.

class Car:
    def __init__(self, make, model, year, initial_mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.__initial_mileage = initial_mileage

    def fullname(self):
        return f"This is a {self.make} {self.model} created in {self.year}"

    def get_millage(self):
        return self.__initial_mileage

    def update_mileage(self, value):
        self.__initial_mileage = value
        return f"The new millage is {value}"


c1 = Car("Toyota", "Hyundai", 2018)
c1.update_mileage(250)
print(c1.get_millage())
