# 14. Method Encapsulation
#     Encapsulate a method in the Car class that calculates depreciation based on the car age and is only accessible
#     within the class.

class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def __depreciation(self, year):
        self. age = 2024 - year
        if self.age <= 2:
            depreciation = 0
        else:
            depreciation = self.age * self.price * 0.08     # simple formula may be not the actual
        return depreciation

    def get_car_dep(self):
        print(self.__depreciation(self.year))


c1 = Car("Toyota", "Hyundai", 2018, 10000)
c1.get_car_dep()
