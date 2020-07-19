from ._condition import Condition
import random

class Temperature(Condition):
	'''
	'''
	def __init__(self, init_value, status_dict):
		super().__init__(init_value, status_dict)
		self.lower = 22
		self.upper = 25

	def generate_info(self):
		''' This function is to generate the temperature information which includes
			the degrees Celsius of temperature and its rewarding status.

		>>> temperature = Temperature(20)
		>>> temperature.set_range(22, 25)
		>>> temperature.generate_info()
		{"temperature": 23.5, "status": "Perfect"}
		'''
		new_value = self.init_value + random.uniform(-1, 1) * 6
		status = self._map_condition(new_value)

		return { "temperature": new_value, "status": status }