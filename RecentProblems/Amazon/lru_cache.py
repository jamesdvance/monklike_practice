"""
Using sorted dict data structure
"""


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity 
        

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)
            return self(key)
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last=False)


"""
Using dictionary and linked list
"""
class ListNode:
    def __init__(self,key, val, next=None, prev=None):
        self.key = key
        self.val = val 
        self.next = self.prev = None
        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next = self.right 
        self.right.prev = self.left

    def remove(self,node):
        # removes from linked list
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev 

    def insertRight(self, node):
        # inserts into linked list behind self.right
        prev, nxt = self.right.prev, self.right 
        prev.next = nxt.prev = node 
        node.next, node.prev = nxt, prev 

    def get(self, key:int)->int:
        if key in self.cache:
            self.remove(self.cache[key]) # re
            self.insertRight(self.cache[key])
            return self.cache[key].val 

        else:
            return -1

    def put(self,key:int, val:int):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key, val)
        self.insertRight(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key] # why we need its key stored in the node

