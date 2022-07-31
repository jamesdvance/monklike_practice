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
            nonlocal first
            nonlocal last
            if not node:
                return 
            # First DFS Left 
            dfs(node.left)
            # Finally, add to list
            if last:
                last.right = node 
                node.left = last 
            else:
                first = node 
            # Next, DFS Right
            last = node 
            dfs(node.right)

        last, first = None, None
        dfs(root)
        last.right = first 
        first.left = last 
        return first 
