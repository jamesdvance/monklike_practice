"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:

LFUCache(int capacity) Initializes the object with the capacity of the data structure.
int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When the cache reaches its capacity, 
it should invalidate and remove the least frequently used key before inserting a new item. For this problem, 
when there is a tie (i.e., two or more keys with the same frequency), the least recently used key would be invalidated.
To determine the least frequently used key, a use counter is maintained for each key in the cache. T
he key with the smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). 
The use counter for a key in the cache is incremented either a get or put operation is called on it.

The functions get and put must each run in O(1) average time complexity.
"""
class Node:

    def __init__(self,count_=1, prev=None, next_=None):
        self.count_=count_
        self.prev = prev
        self.next_ = next_

# Starting Given Cache
class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {} # user-provided key -> pointer to LinkedList Node
        self.value_counts = {} # count of total frequency -> pointer to most recent LinkedListNode with that count
        self.capacity = capacity
        self.minFreq =1 

    def _update_list_by_count(self,):
        """
        Updates List of counter
        """
        pass

    def _add_at_head(self):
        pass 

    def _remove_node(self):
        pass        

    def get(self, key: int) -> int:
        """
        Starts with 
        """

    def put(self, key: int, value: int) -> None:
        """
        Uses a data structure to maintain the frequently used property
        A LinkedList would work 
        """
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

