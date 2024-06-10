# 6. Using `super()`
#    Modify the ElectricCar class so that it uses super() to call the __init__() of the Car class.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def fullname(self):
        return f"This is a {self.make} {self.model} created in {self.year}"


class Electric_Car(Car):
    def __init__(self, make, model, year, battery_size):
        super(). __init__(make, model, year)
        self.battery_size = battery_size

    def fullname(self):
        return (f"This is a {self.make} {self.model} with a battery size"
                f" of {self.battery_size} and created in {self.year}")


c1 = Car("Toyota", "Hyundai", 2018)
c2 = Electric_Car("Ford", "Mustang", 2005, 12)
print(c2.fullname())
