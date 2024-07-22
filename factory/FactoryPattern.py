from abc import ABC, abstractmethod

# Abstract base class for Car
class Car(ABC):
    @abstractmethod
    def make(self):
        pass

# Concrete classes implementing the Car interface
class Sedan(Car):
    def make(self):
        print("Making a Sedan")

class Hatchback(Car):
    def make(self):
        print("Making a Hatchback")

# Abstract Factory class
class CarFactory(ABC):
    @abstractmethod
    def create_car(self):
        pass

# Concrete factory for creating Sedan cars
class SedanFactory(CarFactory):
    def create_car(self):
        return Sedan()

# Concrete factory for creating Hatchback cars
class HatchbackFactory(CarFactory):
    def create_car(self):
        return Hatchback()

def FactoryPattern(factory: CarFactory):
    car = factory.create_car()
    car.make()

# Usage
sedan_factory = SedanFactory()
hatchback_factory = HatchbackFactory()

FactoryPattern(sedan_factory)
FactoryPattern(hatchback_factory)