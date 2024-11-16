"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
	cargo = 0
	max_cargo = 0

	def __init__(self, weight, fuel, fuel_consumption, max_cargo):
		Vehicle.__init__(self, weight, fuel, fuel_consumption)
		self.max_cargo = max_cargo

	def load_cargo(self, additional_cargo):
		if self.max_cargo >= self.cargo + additional_cargo:
			self.cargo += additional_cargo
			return self.cargo
		else:
			raise CargoOverload("Weight of cargo can't be so many!")

	def remove_all_cargo(self):
		previous_cargo = self.cargo

		self.cargo = 0

		return previous_cargo