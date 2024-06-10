# 10. Create a class with composition
#     Define two classes, Engine and Body, then use these to form a composite class Car that includes an engine
#     and a body.

class Engine:
    def __init__(self, automatic):
        self.automatic = automatic

    def start(self):
        return "Engine Started"

    def stopped(self):
        return "Engine is stopped"

class Body:
    def __init__(self, color):
        self.color = color

    def slider_doors(self):
        return "doors are slider"

class Car:
    def __init__(self, make, model, year, automatic, color):
        self.make = make
        self.model = model
        self.year = year
        self.engine = Engine(automatic)
        self.body = Body(color)

    def start(self):
        return self.engine.start()

    def stopped(self):
        return self.engine.stopped()

    def slider_doors(self):
        return self.body.slider_doors()

    def fullname(self):
        return (f"This is an {self.engine.automatic} {self.make} {self.model} with a {self.body.color} color and "
                f"created in {self.year} ")


c1 = Car("Toyota", "Hyundai", 2018, "semi_auto", "Yellow")
print(c1.fullname())
