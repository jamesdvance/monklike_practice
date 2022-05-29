"""
Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Steps: 
Rephrase: Reorder the singly-linekd linkedlist into a merge of the first half and last half, so that 
the first element is the first element of the original and the second element is the last element of the original, etc

Inputs: LinkedList Node, outputs, None (must modified in place )

Data structure: array. An array can store each value and make the merge easier. 

Inputs to test: 
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input head = [1]
Output: [1]

Pseudo:
Iterate once through singly linked list, writing values to an array in order

#Initialize a sentital node to point to head. 

Iterate backwards over array, until reaching len(arr)//2 steps. 
During each step. take the existing head's next node and copy it to head.old_next. 
initialize new node and point head.next to it. set that node's next to head's old_next
delete head's old_next
set newest node to head's old next. 

Repeat

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        node = head
        node_arr = []
        while node: 
            node_arr.append(node)
            node=node.next 

        even_len = True if len(node_arr)%2==0 else False
        stop_point = len(node_arr)//2 if even_len else (len(node_arr)-1)//2
        node=  head # shallow copy
        for i in range(len(node_arr)-1,
            stop_point,
             -1):
            old_next = node.next 
            node.next = node_arr[i]
            node.next.next = old_next 
            node = node.next.next 
        
        if even_len:
            node = node.next
            node.next = None 

        else:
            node.next=None