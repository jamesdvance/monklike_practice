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

            leftmost.left.next = leftmost.right 

            if leftmost.next:
                leftmost.right.next = leftmost.next.left

            leftmost = leftmost.left

        return root 


