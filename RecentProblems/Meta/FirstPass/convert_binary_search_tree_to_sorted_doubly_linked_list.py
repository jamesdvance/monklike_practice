"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        def dfs(node):
            nonlocal last
            nonlocal first
            if not node:
                return 

            # Inorder
            dfs(node.left)

            if last:
                last.right = node # makes node, second to last
                node.left = last

            else:
                first = node # no last means this is the first iteration 

            last = node 

            dfs(node.right)


        last, first = None, None 

        dfs(root)
        # Complete the circle
        last.right = first 
        first.left = last 
        return first