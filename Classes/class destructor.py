# 15. Create a destructor
#     Implement the __del__ method in the Car class to print a message when a car instance is being deleted.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        return "Must be driven on land"

    def __del__(self):
        print("This class is no more")


c1 = Car("Toyota", "Hyundai", 2018)
