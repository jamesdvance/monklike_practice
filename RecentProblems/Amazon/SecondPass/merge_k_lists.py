# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        head = point = ListNode(0)
        q= PriorityQueue()
        for l in lists:
            if l:
                q.put((l.val, l))

        while not q.empty():
            val, node = q.get()
            point.next = ListNode(val)
            