"""
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]

Plan: Iterate through list with a two-pointers, once going two ahead to find the end. 
Build a backward pointer as move. once find the end, calculate n, and go to n-1
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        sentinal = ListNode(next=head)
        lead = sentinal 
        follow = sentinal 

        for i in range(n):
            lead = lead.next

        while lead.next:
            lead = lead.next 
            follow=follow.next 

        follow.next = follow.next.next 

        return sentinal.next 
