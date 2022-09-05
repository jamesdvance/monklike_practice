# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:

        def dfs_left(node):
            if not node or (not node.right and not node.left):
                # don't want to append the leaves, since they're covered below
                return 

            boundary.append(node.val)
            if node.left:
                dfs_left(node.left)
            else:
                dfs_left(node.right)


        def dfs_leaves(node):
            if not node:
                return 

            dfs_leaves(node.left) # want to find leftmost leaves first
            if node != root and not node.right and not node.left:
                boundary.append(node.val)
                return 

            dfs_leaves(node.right)

        def dfs_right(node):
            if not node or (not node.right and not node.left):
                return 

            if node.right:
                dfs_right(node.right)
            else:
                dfs_right(node.left)
            
            boundary.append(node.val)


        boundary = [root.val]
        dfs_left(root.left)
        dfs_leaves(root)
        dfs_right(root.right)

        return boundary



