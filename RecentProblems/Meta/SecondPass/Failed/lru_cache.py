# OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self:
            val = self[key]
            self.move_to_end(key)
        else:
            val = -1

        return val 

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end[key]
            self[key]= value 
        else:
            self[key]=value 
            if len(self) > self.capacity:
                self.popitem(last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
class Node:
    def __init__(self, val=0, nxt=None, prev=None):
        self.val=val
        self.prev = prev
        self.next =nxt 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head=Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size= 0

    def _add_node(self, node):
        " Inserts a node behind last node after head"
        new = self.head.next 
        if new:
            node.next = new 
            new.prev = node 
            self.head.next = node 
            node.prev = self.head
            self.size+=1
        else:
            self.head.next = node 
            node.prev = self.head

    def _remove_node(self,node):
        new = node.next 
        prev = node.prev 
        prev.next = new
        new.prev = prev

    def _move_to_end(self, node):
        self._remove_node(node)
        self._add_node(node)

    def _pop_last(self):
        new_last = self.tail.prev.prev 
        new_last.next = self.tail 
        self.tail.prev = new_last

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        else:
            node = self.cache[key] 
            self._move_to_end(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value 
            self._move_to_end(node)
        else:
            node = Node(val=value)
            self._add_node(node)
            self.cache[key] = node
            if self.size > self.capacity:
                self._pop_last()        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
