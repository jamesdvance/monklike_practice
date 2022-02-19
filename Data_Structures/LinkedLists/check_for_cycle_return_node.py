# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            node.seen = True
            old_node = node
            node = node.next
            if hasattr(node, 'seen') \
                and not hasattr(node, 'prev'):
                return node
            elif hasattr(node, 'prev') and node.prev != old_node:
                return node
            else:
                node.prev = old_node
        
        return