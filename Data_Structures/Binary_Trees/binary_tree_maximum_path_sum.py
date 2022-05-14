"""
Start: 9:32 PM
End: 9:50 
Solve Time: 3 days
Runs Before successful:  5-10
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def maxPathSum(self, root: Optional[TreeNode]) -> int:
		"""
		Notes: 
		1. will need to check if is path
		2. Then, will need to track the maximum value
		3. If no nodes are negative, then they the whole sum is the max
		3. Reminds of other problems like binary tree to linked list

		Approach: 
		Iterate using inorder traversal, checking if the sum is appropriate

		Always do an eye debug - Adaeb
		"""
		self.max_sum = root.val 
		
		self.curPathSum(root)

		return self.max_sum

	def curPathSum(self, root:TreeNode)->tuple:
		"""Postorder traversal """
		if not root:
			return None 

		# Is a postorder process
		left_sum = self.curPathSum(root.left)
		right_sum = self.curPathSum(root.right)

		sum_list = [root.val]
		if left_sum:
			sum_list.append(left_sum+root.val)
		if right_sum:
			sum_list.append(right_sum+root.val)

		cur_sum = max(sum_list)
		if not right_sum:
			right_sum = 0

		if not left_sum:
			left_sum =0

		self.max_sum = max(cur_sum, 
			self.max_sum,
			right_sum+left_sum+root.val)

		return cur_sum






