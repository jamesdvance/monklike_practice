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
        """
        Need to return a true deep copy
        Thoughts:
        1. Seems like it should be simple. Iterate through the orignal list and update the new list with
            what is seen. 
        2. Steps:
            1. Get List Length O(N)
            2. Create Deep Copy List without Randoms O(N)
            3. Iterate and add Random Nodes O(N)
        """
        if not head:
            return head
        
        def getNodeIndex(search_node, node):
            index=0
            while search_node != node:
                search_node= search_node.next 
                index+=1
            
            return index
                
        def searchIndex(search_node, index):
            n =0
            while n < index:
                search_node = search_node.next
                n +=1
                
            return search_node
            
        # 2. Create Deep Copy List W/Out Randoms
        deep_head = Node(x=head.val) # don't start with next or random
        deep_node = deep_head # shallow copy
        node = head
        while node.next:
            if node.next:
                deep_node.next = Node(x=node.next.val)
            
            # Increment
            node = node.next
            deep_node = deep_node.next
            
        # 3. Add Randoms into list
        node = head
        deep_node = deep_head # shallow copy
        while node:
            if node.random:
                rand_idx = getNodeIndex(head, node.random)
                deep_node.random = searchIndex(deep_head,rand_idx)
            
            node = node.next
            deep_node = deep_node.next
            
        return deep_head      