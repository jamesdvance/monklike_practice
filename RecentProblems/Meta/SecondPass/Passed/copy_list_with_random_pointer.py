"""
Approach: iterate over linked list 
2. Use a dictionary to lookup 

Brute force would be something like copying the entier linkedlist with one pass
Then, going through and using O(N) find on each random node
O (N**2)

"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        ref_dict = {}
        node = head
        while node:
            node_copy = ref_dict.get(node,None)
            if not node_copy:
                node_copy =Node(x=node.val)
                ref_dict[node] = node_copy
            if node.random:
                rand_copy = ref_dict.get(node.random, None)
                if not rand_copy:
                    rand_copy = Node(x=node.random.val)
                    ref_dict[node.random] = rand_copy
                node_copy.random=rand_copy
            if node.next:
                next_copy = ref_dict.get(node.next, None)
                if not next_copy:
                    next_copy = Node(x=node.next.val)
                    ref_dict[node.next]=next_copy
                node_copy.next = next_copy
            node=node.next 

        return ref_dict[head]






