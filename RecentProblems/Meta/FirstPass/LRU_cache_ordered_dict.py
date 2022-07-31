from collections import OrderedDict 
class LRUCache(OrderedDict):

	def __init__(self,capacity):
		self.capacity = capacity 


	def get(self, key):
		if key in self:
			self.move_to_end(key)
			return self[key]

		else:
			return -1 

	def put(self, key, value):

		if key in self: 
			self.move_to_end(key)
			
		self[key] = value 
		if len(self) > self.capacity:
			self.popitem(last=False)
