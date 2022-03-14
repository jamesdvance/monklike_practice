# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        right_depth = 0
        left_depth = 0
        if root.right and root.left:
            right_depth += self.maxDepth(root.right) + 1
            left_depth += self.maxDepth(root.left) + 1
            return max([right_depth, left_depth])
        elif root.right:
            right_depth += self.maxDepth(root.right) + 1
            return right_depth
        elif root.left:
            left_depth += self.maxDepth(root.left)+1
            return left_depth
        else:
            return 1