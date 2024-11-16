from abc import ABC
from homework_02.exceptions import LowFuelError
from homework_02.exceptions import NotEnoughFuel


class Vehicle(ABC):
    weight = 0
    fuel = 0
    fuel_consumption = 0
    started = False

    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started and self.fuel > 0:
            self.started = True
            return self.started
        else:
            raise LowFuelError ("You can't start without fuel!")

    def move(self, distance):
        required_fuel = self.fuel_consumption * distance 

        if self.fuel >= required_fuel:
            self.fuel -= required_fuel
            return self.fuel
        else:
            raise NotEnoughFuel ("The fuel is not enough!")