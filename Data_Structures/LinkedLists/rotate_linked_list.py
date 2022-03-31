# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        If K > length of list, total rotations is k%length of list
            1. Cycle through list, if get to k, set next to none and next to new_head
            2. 
        """
        
        # 
        if not head:
            return None
        
        length = 1
        node = head
        while node.next:
            length+=1
            node = node.next 
            
        print(length)
            
        if k == length:
            return head
        
        # Set final item of list to 
        node.next = head
        
        if k < length:
            stop = length - k 
        elif length < k:
            stop = length - k%length
            
        index = 1 
        node = head
        while node:
            if index == stop:
                head = node.next
                node.next = None
                break
            
            node = node.next
            index+=1
            
        return head