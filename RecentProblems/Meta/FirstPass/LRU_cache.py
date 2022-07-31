class DLinkedNode():

	def __init__(self,value=None):
		self.prev = None 
		self.next = None 
		self.value = value

class LRUCache():

	def __init__(self, capacity):
		self.capacity = capacity
		self.head = DLinkedNode()
		self.tail = DLinkedNode()
		self.head.next = self.tail 
		self.tail.prev = self.head 
		self.cache = {}
		self.size =0 

	def _add_node(self,node):
		new = self.head.next 
		node.next = new
		new.prev = node 
		self.head.next = node 

	def _remove_node(self,node):
		new = node.next 
		prev = node.prev 
		prev.next = new 
		new.prev = prev 

	def _move_to_end(self, node):
		self._remove_node(node)
		self._add_node(node)

	def _pop_last(self):
		new_last_item= self.tail.prev.prev 
		new_last_item.next = self.tail 
		self.tail.prev = new_last_item

	def get(self, key):
		if key not in self.cache: 
			return -1 
		else:
			node = self.cache[key]
			self._move_to_end(node)
			return node.value 

	def put(self,key,value):
		if key in self.cache:



		else: