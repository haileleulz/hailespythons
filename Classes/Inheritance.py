# 4. Inheritance
#    Create a ElectricCar class that inherits from the Car class and adds a new attribute for battery size and a
#    method to display this information.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def fullname(self):
        return f"This is a {self.make} {self.model} created in {self.year}"


class Electric_Car(Car):
    def __init__(self, make, model, year, battery_size):
        Car. __init__(self, make, model, year)
        self.battery_size = battery_size


c1 = Car("Toyota", "Hyundai", 2018)
ec1 = Electric_Car("Abay", "Tana",2020, 12)
print(ec1.fullname())
