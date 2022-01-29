# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Will try the two-pointer technique"""
        
        head.step = 1
        if not head:
            return None
        
        if not head.next and n==1:
            return None
        
        node_one_step = head
        node_two_step = head
        while node_two_step.next and node_two_step.next.next:
            #two step
            old_node_two_step = node_two_step
            node_two_step = node_two_step.next.next
            node_two_step.step =old_node_two_step.step + 2
            node_two_step.prev = old_node_two_step
        
        if node_two_step.next:
            #two step
            old_two_step = node_two_step.step
            node_two_step = node_two_step.next
            node_two_step.step =old_two_step+1
        
        length = node_two_step.step
        erase_idx = length - n # erase_index is zero indexed
        """
        head_idx = 0
        tail_idx = length -1
        one_step_idx = node_one_step.step -1 
        def abs_val(digit):
            if digit < 0:
                return digit*-1
            else:
                return digit
        distances= [abs_val(erase_idx-head_idx), 
            abs_val(erase_idx-one_step_idx),
            abs_val(erase_idx - tail_idx)]
        
        shortest_res = distances.index(min(distances))
        if shortest_res == 0: 
            # head
            erase_node = head
            direction = 'next'
            while erase_node.step < erase_idx+1
                
        elif shortest_res == 1:
            # one-step
        else:
            # tail
            erase_node = node_two_step
        """
        erase_node = head
        erase_node.index =0
        if erase_idx == 0:
            return erase_node.next
        
        while (erase_node.index) < erase_idx-1:
            old_idx = erase_node.index
            erase_node = erase_node.next
            erase_node.index = old_idx+1
        # Deletion
        prev_node = erase_node
        prev_node.next = erase_node.next.next
            
        return head

"""
This is my still-buggy attempt at speeding up the above code with a two-pointer technique. It wasn't as elegant or fast as 
the correct approach with using a pointer n steps ahead of the original. 
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """Will try the two-pointer technique"""
        
        head.step = 1
        if not head:
            return None
        
        if not head.next and n==1:
            return None
        
        node_one_step = head
        node_two_step = head
        two_step_head = node_two_step
        two_step_head.next = node_two_step.next.next
        
        while node_two_step.next and node_two_step.next.next:
            # two step
            old_node_two_step = node_two_step
            node_two_step = node_two_step.next.next
            node_two_step.step =old_node_two_step.step + 2
            node_two_step.prev = old_node_two_step
            # one step
            old_node_one_step = node_one_step
            node_one_step = node_one_step.next
            node_one_step.step =old_node_one_step.step + 1
            node_one_step.prev = old_node_one_step
            
        if node_two_step.next:
            #two step
            old_two_step = node_two_step.step
            node_two_step = node_two_step.next
            node_two_step.step =old_two_step+1
        
        length = node_two_step.step
        erase_idx = length - n # erase_index is zero indexed
        if erase_idx == 0:
            return head.next
        
        # Choosing direction
        head_idx = 0
        tail_idx = length -1
        one_step_idx = node_one_step.step -1 
        def abs_val(digit):
            if digit < 0:
                return digit*-1
            else:
                return digit
        distances= [abs_val(int((erase_idx-head_idx)/2)), 
            abs_val(erase_idx-one_step_idx),
            abs_val(int((erase_idx - tail_idx)/2))]
        
        shortest_res = distances.index(min(distances))
        if shortest_res == 0: 
            # head
            erase_node = two_step_head
            direction = 'next'
            step_size=2
            erase_node.index=0
                
        elif shortest_res == 1:
            # one-step
            erase_node = one_step_node
            if erase_idx > one_step_idx:
                direction='next'
            else:
                direction='prev'
            
            step_size=1
            erase_node.index=erase_node.step-1
            
        else:
            # tail
            erase_node = node_two_step
            step_size=2
            direction='prev'
            erase_node.index = (erase_node.step-1)/2

        if direction == 'next':
            while (erase_node.index) < erase_idx-1:
                old_idx = erase_node.index
                if step_size ==2:
                    erase_node = erase_node.next.next
                else:
                    erase_node = erase_node.next
                    
                erase_node.index = old_idx+step_size
                    
            if erase_node.index > erase_idx-1 \
                and step_size==2:
                erase_node = erase_node.prev
                erase_node = erase_node.next
                    
        else:
            while (erase_node.index) > erase_idx-1 and hasattr(erase_node, 'prev'):
                old_idx = erase_node.index
                if step_size ==2:
                    erase_node = erase_node.prev
                else:
                    erase_node = erase_node.prev
                    
                erase_node.index = old_idx-step_size
                    
            if erase_node.index < erase_idx-1:
                erase_node = erase_node.next
                
        # Deletion
        prev_node = erase_node
        erase_node = prev_node.next
        prev_node.next = erase_node.next
            
        return head