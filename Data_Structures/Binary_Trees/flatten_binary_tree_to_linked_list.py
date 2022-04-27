# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import copy
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return root
        
        right = copy.deepcopy(root.right)
            
        if root.left:
            root.right = self.flatten(root.left)
            
        elif right:
            root.right = self.flatten(right)
            
        child = root.right
        while child and child.right:
            child = child.right
            
        if root.left and right:
            "Append into node.right.right"
            child.right = self.flatten(right)
            
        root.left = None
                
                
        return root