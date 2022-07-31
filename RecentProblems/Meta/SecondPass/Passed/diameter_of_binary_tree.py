# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

"""

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:


        def dfs(node):
            nonlocal maxdiam
            if not node:
                return 0

            lpath = dfs(node.left)
            rpath = dfs(node.right)
            maxdiam = max(maxdiam, lpath+rpath)

            return max(lpath, rpath)+1


        maxdiam=0
        dfs(root)
        return maxdiam
        
        


        


