from ._condition import Condition
import random

class Humidity(Condition):
	'''
	'''
	def __init__(self, init_value, status_dict):
		super().__init__(init_value, status_dict)
		self.lower = 90
		self.upper = 100

	def generate_info(self):
		''' This function is to generate the humidity information which includes the
			percentage of humidity and its rewarding status.

		>>> humidity = Humidity(50)
		>>> humdity.set_range(70, 75)
		>>> humidity.generate_info()
		{"humidity": 65.5, "status": "Normal"}
		'''
		new_value = self.init_value + random.uniform(-1, 1) * 20
		status = self._map_condition(new_value)

		return { "humidity": new_value, "status": status }