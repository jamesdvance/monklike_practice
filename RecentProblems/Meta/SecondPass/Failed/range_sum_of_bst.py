# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            nonlocal ret_sum
            if not node:
                return 
            if low <= node.val <= high:
                ret_sum+=node.val
            if low < node.val:
                dfs(node.left)
            if high> node.right:
                dfs(node.right)
            
        ret_sum=0
        dfs(root)
        return ret_sum