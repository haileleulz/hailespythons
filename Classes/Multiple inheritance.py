# 13. Multiple inheritance
#     Create a new class AmphibiousVehicle that inherits from both Car and a new Boat class. Ensure it has methods
#     to drive and sail.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def drive(self):
        return "Must be driven on land"


class Boat:
    def __init__(self, brand, purpose):
        self.brand = brand
        self.purpose = purpose

    def sail(self):
        return "Must be sailed on a water"


class AmphibiousVehicle(Car, Boat):
    def __init__(self, means, make, model, year, brand, purpose):
        self.means = means
        self.car = Car(make, model,year)
        self.boat = Boat(brand, purpose)

    def drive(self):
        return self.car.drive()

    def sail(self):
        return self.boat.sail()


av1 = AmphibiousVehicle("Both","Toyota", "Hyundai", 2018, "Ibiza", "relaxation")
print(av1.drive())
print(av1.sail())
