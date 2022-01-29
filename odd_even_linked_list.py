# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sentinel_odd = ListNode(0)
        sentinel_even = ListNode(0)
        
        prev_odd = sentinel_odd
        prev_even = sentinel_even
        
        curr = head
        itr = 1
        while curr:
            if itr % 2 ==0:
                prev_even.next = curr
                prev_even = curr
                
            else:
                prev_odd.next = curr
                prev_odd = curr
                
            curr = curr.next 
            itr+=1
        
        prev_even.next =None
        prev_odd.next = sentinel_even.next
        return sentinel_odd.next