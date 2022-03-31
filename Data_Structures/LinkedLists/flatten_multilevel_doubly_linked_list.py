"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        if not head:
            return head
    
        if not hasattr(self, "old_next_stack"):
            self.old_next_stack = []
        
        if head.child:
            head.child.prev = head
            if head.next:
                self.old_next_stack.append(head.next)
                
            head.next = self.flatten(head.child)
            head.child = None

        elif head.next:
            head.next = self.flatten(head.next)
        
        elif len(self.old_next_stack)>0:
            new_next = self.old_next_stack.pop(len(self.old_next_stack)-1)
            new_next.prev = head
            head.next = self.flatten(new_next)
                
        

        return head