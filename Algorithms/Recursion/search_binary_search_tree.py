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

        Approach: 
        1. Need to keep track of whether 
        """

        if not root.right and not root.left:
            return 

        if root.val == val:
            return root

        if root.right:
            return_node = self.searchBST(root.right,val)

        if not return_node and root.left:
            return_node = self.searchBST(root.left,val)

        return return_node

