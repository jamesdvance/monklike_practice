# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        You are given the root of a binary search tree (BST) and an integer val.

        Find the node in the BST that the node's value equals val and return the 
        subtree rooted with that node. If such a node does not exist, return null.

        """
        if root is None or val == root.val:
            return root 

        return self.searchBST(root.left, val) if val < root.val \
            else self.searchBST(root.right, val)

"""
Iterative Solution
"""
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right 

        return root 