class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.meter = 0
        
    def get_description(self):
        info = f"{self.make} {self.model} {self.year} {self.meter}"
        return info.title()
    
    def updateMeter(self, mileage):
        self.meter = mileage

mycar = Car("tesla", 'model S', 2021)
yourcar = Car('Fiat', 'Panda', 2021)

mycar.get_description()
yourcar.get_description()

mycar.updateMeter(20000)
mycar.get_description()