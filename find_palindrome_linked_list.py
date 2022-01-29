# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head.next:
            return True
        
        prev = None
        curr = head
        curr.prev = prev
        
        while curr.next:
            prev=  curr
            curr = curr.next
            curr.prev = prev
        
        # Iterate from original head and from backward_tail
        while curr.prev and head.next:
            if head.val != curr.val:
                return False
            else:
                head = head.next
                curr = curr.prev
        
        if not curr.prev and not head.next:
            return True
        else:
            return False
            