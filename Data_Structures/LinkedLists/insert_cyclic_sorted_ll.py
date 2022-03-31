"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        """Approach: 
            1. Cycle through list, adding prev pointer
            2. Once reach point where prev < insertVal and cur > insert_val OR the opposite, insert the node
        """
        if not head:
            node = Node(val=insertVal)
            node.next = node
            return node
        
        if head.next == head:
            head.next = Node(val=insertVal, next=head)
            return head 
        
        prev = head
        node = head.next # shallow copy

        """
        Check if:
            1. Node between current vals and it makes sense from an ascending/descending persective
        """
        prev.marker = True
        while node:
            if node.val < prev.val:
                if insertVal > prev.val or insertVal < node.val:
                    break
                    
            elif prev.val <= insertVal and insertVal <= node.val:
                break
            
            prev = node
            node = node.next
            
            if hasattr(node, "marker"):
                break
            # Change asc to desc. If change, 
            
        prev.next = Node(val=insertVal, next=node)
            
        return head
            