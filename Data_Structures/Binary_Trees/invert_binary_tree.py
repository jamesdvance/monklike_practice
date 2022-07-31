# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Seems like two possible solutions: 
DFS to that terminates at leaf nodes, and then for each other node, swap the children
BFS where each levele gets added to a list and then reversed

"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return 

        if not root.right and not root.left:
            return root 

        placeholder = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        root.left = placeholder

        return root 

"""
BFS
"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None 

        queue = collections.deque
        while queue:
            current=queue.popleft()
            current.left, current.right = current.right, current.left 

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return root 