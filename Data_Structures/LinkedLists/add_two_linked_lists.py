# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l1_str = ''
        while l1.next:
            l1_str =str(l1.val)+l1_str
            l1 = l1.next
        l1_str = str(l1.val) +l1_str
        
        l2_str = ''
        while l2.next:
            l2_str =str(l2.val)+l2_str
            l2 = l2.next
        l2_str = str(l2.val) +l2_str
        l1_int = int(l1_str)
        l2_int = int(l2_str)
        new_str = str(l1_int+l2_int)
        #str_rev= new_str[::-1]
        next_node = ListNode(new_str[0])
        for i in range(1,len(new_str)-1):
            new_node = ListNode(new_str[i])
            new_node.next = next_node
            next_node = new_node
        if len(new_str)>1:
            new_node = ListNode(new_str[len(new_str)-1]) # last item in the int
            new_node.next = next_node
            return new_node
        else:
            return next_node
        