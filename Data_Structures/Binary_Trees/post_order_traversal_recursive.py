# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return_list = []
        if root:
            if root.left:
                return_list+=self.postorderTraversal(root.left)
            if root.right:
                return_list+=self.postorderTraversal(root.right)

            if root.val:
                return_list.append(root.val)
        
        return return_list