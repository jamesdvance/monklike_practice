# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        def dfs(node, lvl):
            if not node:
                return
            nonlocal vals
            nonlocal max_lvl
            # Left first 
            dfs(node.left,lvl+1)
            vals[lvl] = node.val
            dfs(node.right, lvl+1)
            max_lvl = max(lvl,max_lvl)

        vals = {}
        max_lvl = 0
        dfs(root,0)
        return [vals[i] for i in range(max_lvl+1)]

