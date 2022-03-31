"""
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate 
each next pointer to point to its next right node, just like in Figure B.
The serialized output is in level order as connected by the next pointers, with '#' signifying
 the end of each level.
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Iterates through and challenges all newcomers

        if not root:

            return root

        leftmost = root # shallow copy

        while leftmost.left:

            # Assign 'head' to ensure we can iterate through entire level

            head = leftmost 

            while head:

                head.left.next = head.right 

                if head.next:
                    head.right.next = head.next.left

                head = head.next 

            leftmost = leftmost.left

        return root 


