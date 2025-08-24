
"""
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
"""

# Code Template
class AllOne(object):

    def __init__(self):
        pass

    def inc(self, key):
        """
        Increments the count of the string by 1. Adds if not exists

        :type key: str
        :rtype: None

        """
        

    def dec(self, key):
        """
        Decrements string count by 1. Removes if 0
        :type key: str
        :rtype: None
        """
        

    def getMaxKey(self):
        """
        Return any key with the max count. If nothing exists, return empty string
        :rtype: str
        """
        

    def getMinKey(self):
        """
        Return any key with the min count. If nothing exists, return empty string
        :rtype: str
        """
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

"""

Blind Attempt
"""

class Node:

    def __init__(self, count=0, string=""):
        self.prev = None
        self.next = None 
        self.count= count
        self.string = string
        

class AllOne(object):
    """
    This is like Least Recently Used Cache. We need a way
    to track the order of the keys by the count in order to return in O(1) time
    # tail -> node(1) -> node(1) -> node(3) -> node(4) -> head

    # Got pretty close - passed 22 /24 test cases. Moving on
    """

    def __init__(self):
        self.head =Node()
        self.tail = Node()
        self.head.prev = self.tail 
        self.tail.next = self.head
        self.strings = {} # string -> node
        

    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """

        if key not in self.strings:
            orig_next = self.tail.next
            new = Node(count=1, string=key)
            orig_next.prev = new
            new.next = orig_next 
            new.prev = self.tail
            self.tail.next = new
            self.strings[key] = new

        else:
            node = self.strings[key]
            node.count+=1
            while node.count > node.next.count and node.next.string != "":

                orig_next = node.next 
                new_next = orig_next.next 
                orig_prev= node.prev

                new_next.prev = node 
                self.strings[new_next.string] = new_next 
                node.next = new_next 

                orig_next.next = node
                orig_prev.next = orig_next 
                orig_next.prev = orig_prev 

                self.strings[orig_next.string] = orig_next
                self.strings[orig_prev.string] =  orig_prev

                node.next = new_next 
                node.prev = orig_next 

            self.strings[key] = node

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """

        if key not in self.strings:
            # duh not needed
            node = Node(count=1, string=key)
            node.next = self.tail.next 
            self.tail.next.prev = node
            node.prev = self.tail
            self.tail.next = node 
            self.strings[key] = node

        else:
            node = self.strings[key]
            node.count -= 1
            if node.count == 0:
                node.prev.next = node.next 
                node.next.prev = node.prev 
                self.strings[node.prev.string] = node.prev
                self.strings[node.next.string] = node.next 
                del self.strings[key]

            else:
                while node.count < node.prev.count:
                    new_prev = node.prev.prev
                    new_next = node.prev
                    new_next.next = node.next
                    new_next.prev = node 
                    self.strings[new_next.string] = new_next
                    node.next = new_next
                    new_prev.next = node
                    self.strings[new_prev] = new_prev
                    node.prev = new_prev 

                self.strings[key] = node
        

    def getMaxKey(self)->str:
        """
        :rtype: str
        """
        return self.head.prev.string
        

    def getMinKey(self)->str:
        """
        :rtype: str
        """
        return self.tail.next.string



def test_all_one():

    all = AllOne()

    assert all.getMaxKey() == ""
    assert all.getMinKey() == ""

    node = all.tail
    while node:
        print(f" {node.string}, cnt: {node.count}")
        node = node.next 

    all.inc("T")
    all.inc("A")

    assert all.getMaxKey() == "A" or all.getMaxKey() == "T"

    all.inc("T")

    assert all.getMaxKey() == "T"

    all.inc("A")

    all.inc("B")

    assert all.getMinKey() == "B"

    all.dec("A")

    node = all.tail 

    while node:
        print(f" {node.string}, cnt: {node.count}")
        node = node.next 

    all.inc("B")

    assert all.getMinKey()  =="A", f"Error in {all.getMinKey()} Here's the min key: {all.tail.next.string} with count {all.tail.next.count} and next key {all.tail.next.next.string} and count {all.tail.next.next.count}"

    all.dec("A")

    assert all.getMinKey() == "B"

test_all_one()
