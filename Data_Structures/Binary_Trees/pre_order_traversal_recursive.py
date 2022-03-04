# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return_list = []
        if root:
            if root.val:
                return_list.append(root.val)
            if root.left:
                return_list+=self.preorderTraversal(root.left)
            if root.right:
                return_list+=self.preorderTraversal(root.right)

            
        return return_list