# 8. Create a class method
#    Add a class method to the Car class that keeps track of the total number of car instances created.

# In this case we need a class variable and we initialize it to the init method to keep counting the number of
# instances created.
class Car:

    total_cars = 0

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.total_cars += 1

    def fullname(self):
        return f"This is a {self.make} {self.model} created in {self.year}"

    @staticmethod
    def classic_or_not(year):
        if year < 1980:
            return "Classic"
        return "Not Classic"

    @classmethod
    def get_total_cars(cls):
        return cls.total_cars


c1 = Car("Toyota", "Hyundai", 2018)
c2 = Car("Ford", "Mustang", 2005)
print(c1.get_total_cars())
