# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return []

        def dfs(node,leaf_str):
            nonlocal sum_arr
            if not node:
                ret_arr.append(int(leaf_str))
                return 

            leaf_str+=str(node.val)
            dfs(node.left, leaf_str)
            dfs(node.right,leaf_str)

        sum_arr = []
        dfs(root,"")
        return sum_arr