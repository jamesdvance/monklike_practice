"""
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].

Example 1:


Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
Example 2:


Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.
"""
# Definition for a binary tree node.
# class TreeNode:
#	 def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

	def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

		def dfs(node):
			nonlocal ans 
			if node:
				if low <= node.val <= high:
					ans+=node.val 
				if low < node.val:
					dfs(node.left)
				if high > node.val:
					dfs(node.right)

		ans =0
		dfs(root)
		return ans


"""
Bottom-up solution
"""
class Solution:
    def rangeSumBST(self, root, L, R):
        if not root:
            return 0;

        if R < root.val:
            return self.rangeSumBST(root.left, L, R)
        elif L > root.val:
            return self.rangeSumBST(root.right, L, R)
        else:
            return self.rangeSumBST(root.left, L, R) + root.val + self.rangeSumBST(root.right, L, R)