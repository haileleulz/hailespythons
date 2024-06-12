# 7. Defining a static method
#    Add a static method to the Car class that takes a year and returns whether the car is considered a classic
#    (25 years or older).

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def fullname(self):
        return f"This is a {self.make} {self.model} created in {self.year}"

    @staticmethod
    def classic_or_not(year):
        if year < 1999:
            return "Classic"
        return "Not Classic"


c1 = Car("Toyota", "Hyundai", 2018)
c2 = Car("Ford", "Mustang", 2005)
print(c1.classic_or_not(1979))
print(c2.classic_or_not(1995))
