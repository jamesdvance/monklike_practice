# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# My solution
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int, currentSum=0) -> bool:
        if not root:
            return False
        currentSum+=root.val
        if not root.right and not root.left:
            if currentSum == targetSum:
                return True
            else:
                return False
        elif not root.left:
            right_check = self.hasPathSum(root.right, targetSum, currentSum)
            left_check = False
        elif not root.right:
            left_check = self.hasPathSum(root.left, targetSum, currentSum)
            right_check = False
        else:
            right_check = self.hasPathSum(root.right, targetSum, currentSum)
            left_check = self.hasPathSum(root.left, targetSum, currentSum)
        
        if right_check ==True or left_check == True:
            return True
        else:
            return False


# Leetcode solution
class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)