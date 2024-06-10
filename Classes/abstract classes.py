# 12. Abstract classes
#     Create an abstract class Vehicle with an abstract method drive(). Make Car inherit from Vehicle and
#     implement the method.

from abc import ABC, abstractmethod

class Vehicle:
    @abstractmethod
    def drive(self):
        pass

class Car(Vehicle):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        if self.year >= 2005:
            return "The vehicle can be driven at 200 kph"
        else:
            return "The car has max speed of 120 kph"


c1 = Car("Toyota", "Hyundai", 2018)
print(c1.drive())
