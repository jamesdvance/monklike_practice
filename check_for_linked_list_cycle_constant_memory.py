# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        while node and node.next:
            node.seen=True
            node = node.next
            if hasattr(node, 'seen'):
                return True
        
        return False
        