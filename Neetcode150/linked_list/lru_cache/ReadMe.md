# LRU Cache

## Summary

Design a data structure that follows the Least Recently Used (LRU) cache eviction policy. It should support get and put operations in O(1) time.

### Key Points
- Need O(1) lookup: use hash map
- Need O(1) insertion/deletion by recency: use doubly linked list
- Hash map stores key -> node pointer
- Linked list maintains order of use

### Optimal Approach
Combine a hash map with a doubly linked list. Most recently used at head, least recently used at tail.

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Dummy head and tail
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_front(self, node: Node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)
        self._add_to_front(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        if len(self.cache) > self.capacity:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
```

### Complexity
- Time: O(1) for both get and put
- Space: O(capacity) for storing cache entries

---

## Detailed Explanation

### Problem Analysis

An LRU cache evicts the least recently used item when at capacity. We need:
1. Fast lookup by key
2. Fast update of recency order
3. Fast identification of least recently used item

A hash map provides O(1) lookup. A doubly linked list provides O(1) insertion and deletion.

### The Data Structure

```
head <-> node1 <-> node2 <-> node3 <-> tail
         ^                   ^
         most recent         least recent
```

- Head and tail are dummy nodes (simplify edge cases)
- Most recently used is right after head
- Least recently used is right before tail

### Why Store Key in Node?

When evicting, we need to remove from both the linked list and the hash map. The linked list node must store the key so we can delete the correct hash map entry.

### Operations Breakdown

**get(key)**:
1. Look up node in hash map
2. If not found, return -1
3. Move node to front (most recently used)
4. Return value

**put(key, value)**:
1. If key exists, remove old node
2. Create new node
3. Add to hash map and front of list
4. If over capacity, remove LRU (tail.prev) and delete from hash map

### Using Python's OrderedDict

Python's OrderedDict maintains insertion order and provides move_to_end:

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```

This is cleaner but uses a library that implements the same underlying structure.

### Edge Cases
- Capacity of 1
- Updating existing key's value
- Get makes item most recently used
- Eviction when all items have been accessed equally recently

### Real-World Applications

LRU caches are used in:
- Operating system page replacement
- Database buffer pools
- Web browser caches
- CPU caches

### Related Problems
- LFU Cache: evict least frequently used
- Design HashMap: implement hash table from scratch
- Design Linked List: implement linked list from scratch
