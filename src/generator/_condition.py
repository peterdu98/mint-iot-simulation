
class Condition:
	def __init__(self, init_value, status_dict):
		self.init_value = init_value
		self.status_dict = status_dict
		self.upper = 0
		self.lower = 0

	def set_range(self, lower, upper):
		''' This function is to set an ideal lower value and an ideal upper value
		
		:param lower: A desired ideal lower value for modification
		:param upper: A desired ideal upper value for modification
		'''
		self.lower = lower
		self.upper = upper

	def set_init_value(self, value):
		''' This function is to set the intial value for each stage 

		:param value: A desired value for modification
		'''
		self.init_value = value
		
	def _map_condition(self, curr_value):
		perfect = self.status_dict["Perfect"]
		normal = self.status_dict["Normal"]
		not_well = self.status_dict["Not well"]

		if curr_value >= self.lower - perfect and curr_value <= self.upper + perfect:
			return 1.0
		elif curr_value <= self.lower - not_well or curr_value >= self.upper + not_well:
			return 0.0
		
		return 0.5
