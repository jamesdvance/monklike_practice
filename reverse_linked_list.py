# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        node = head.next
        head.next = None
        while node.next:
            orig_next = node.next
            node.next = head
            head = node
            node = orig_next
            
        node.next = head
        head = node
            
        return head


"""
Suggested solution

"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        current_head = head
        while head.next:
            p = head.next 
            head.next = p.next # set head.next to the next-next node
            p.next = current_head # pointing at the next 'head'
            current_head = p
            
        return current_head