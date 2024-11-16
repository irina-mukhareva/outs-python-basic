"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class BaseException (Exception):
	pass

class LowFuelError (BaseException):
	pass

class NotEnoughFuel (BaseException):
	pass

class CargoOverload (BaseException):
	pass