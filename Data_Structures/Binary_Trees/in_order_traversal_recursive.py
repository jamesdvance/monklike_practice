
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return_list = []
        if root:
            if root.left:
                return_list+=self.inorderTraversal(root.left)
            return_list.append(root.val)
            if root.right:
                return_list+=self.inorderTraversal(root.right)
            
        return return_list