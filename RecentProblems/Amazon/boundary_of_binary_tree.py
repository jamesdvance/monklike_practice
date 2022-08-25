"""
The boundary of a binary tree is the concatenation of the root, the left boundary, the leaves ordered from left-to-right, and the reverse order of the right boundary.

The left boundary is the set of nodes defined by the following:

The root node's left child is in the left boundary. If the root does not have a left child, then the left boundary is empty.
If a node in the left boundary and has a left child, then the left child is in the left boundary.
If a node is in the left boundary, has no left child, but has a right child, then the right child is in the left boundary.
The leftmost leaf is not in the left boundary.
The right boundary is similar to the left boundary, except it is the right side of the root's right subtree. 
Again, the leaf is not part of the right boundary, and the right boundary is empty if the root does not have a right child.

The leaves are nodes that do not have any children. For this problem, the root is not a leaf.

Given the root of a binary tree, return the values of its boundary.

 
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
    	def dfs_leftmost(node):
    		# DFS leftmost first ( preorder - stop when you reach a leaf)
    		nonlocal boundary
    		if not node or not node.left and not node.right: # stop at first leaf
    			return 

    		boundary.append(node.val)
    		if node.left:
    			dfs_leftmost(node.left)
    		else: # only go right if there's no left node
    			dfs_leftmost(node.right)


    	def dfs_leaves(node):
    		nonlocal boundary
    		if not node:
    			return 

    		dfs_leaves(node.left)
    		if node != root and not node.left and not node.right:
    			boundary.append(node.val)
    		dfs_leaves(node.right)

    	def dfs_rightmost(node):
    		nonlocal boundary
    		if not node or not node.left and not node.right:
    			return 

            boundary.append(node.val)
    		if node.right:
    			dfs_rightmost(node.right)
    		else:
    			dfs_rightmost(node.left)

    	if not root:
    		return []

    	boundary = [root.val]
    	dfs_leftmost(root.left)
    	dfs_leaves(root)
    	dfs_rightmost(root.right)
    	return boundary
