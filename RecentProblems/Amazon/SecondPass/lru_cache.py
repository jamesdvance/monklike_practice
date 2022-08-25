
# Ordered Dict Method
from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity 

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        else:
            return -1 

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key]=value 
        if len(self) > self.capacity:
            self.popitem(last=False)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# LinkedList Method
# LinkedNode
class LinkedNode:

    def __init__(self, next_=None,prev=None, key=None,val=None):
        self.next_=next_ 
        self.prev = prev 
        self.val=val
        self.key = key 

# Cache 
class LRUCache():

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self._cache = {}
        self.head = LinkedNode()
        self.tail = LinkedNode()
        self.head.next_ = self.tail 
        self.tail.prev = self.head 

    def _add_to_end(self, node):
        old_prev = self.tail.prev 
        self.tail.prev = node 
        node.prev = old_prev 
        old_prev.next =node 
        node.next = self.tail  

    def _delete_node(self,node):
        prev = node.prev
        prev.next_ = node.next_  
        node.next_.prev = prev 
        
    def _move_to_end(self, node):
        # add behind tail 
        self._add_to_end(node)
        # delete from cur position 
        self._delete_node(node)

    def get(self, key: int) -> int:
        if key in self._cache:
            self._move_to_end(self._cache[key])
            return self._cache[key].val 

        else:
            return -1 

    def put(self, key, val):
        if key in self._cache:
            self._move_to_end(self.cache[key])
            node = self.cache[key]
        else:
            node = LinkedNode(key=key,val=val)
            self._cache[key] = node 
            self._add_to_end(node)
            self.capacity-=1 
        if self.capacity < 0:
            oldest = self.head.next 
            self._delete_node(oldest)
            del self._cache[oldest.key]
            self.capacity+=1

