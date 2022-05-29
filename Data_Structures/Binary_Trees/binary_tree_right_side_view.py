
"""
Given the root of a binary tree, imagine yourself standing on the right side of it, 
return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4,6,5]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = []
Output: []

Input: root = [1,null, 3, 4,5, null, 6]

Data structure(S)
levels = {level:[]}
left, root, right

Pseudocode

findRight()

if right:
	rightRight

if left:
	findLeft

levels

"""
from collections import OrderedDict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import OrderedDict
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    	if not root:
    		return []

    	def find_right(node:Optional[TreeNode], level:int):
    		if not node:
    			return 
    		if level not in levels:
    			levels[level] = []

    		if node.left:
    			find_right(node.left, level+1)
    		levels[level].append(node)
    		if node.right:
    			find_right(node.right,level+1)

    	levels =  OrderedDict() # 
    	levels[0] = [root]
    	find_right(root.left,1)
    	find_right(root.right,1)
    	return [val[-1].val for key,val in levels.items()]

"""
Leetcode Breadth-first solution

BFS using a queue

1. Push the root into the queue
2. Pop-out a node from the left
3. push the left child into the queue, then push the right child

3 Ways to solve the right side problem using BFS
1. Two queues, one for prev level, one for current
2. One queue with sentiel to mark the end of the level
3. One queue + level size measurement 

Two queues pseudo:
Intiate the list of right side view right_side
Inititate two queues: one for current level (currLevel) and one for the next (nextLevel)
Add root into nextLevel queue
while currentLevel is not empty:
	pop out a node from the currLevel
	Add first left, then right child node into nextLevel queue
when while loop stops, the node that was just popped was the last one in currLevel, so add it to right_side

repeat
"""
# Two queues solution
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    	if root is None:
    		return []

    	next_level = deque([root,])
    	rightside = []

    	while next_level:
    		curr_level = next_level 
    		next_level = deque()

    		while curr_level:
    			node = curr_level.popleft()
	    		if node.left:
	    			next_level.append(node.left)
	    		if node.right:
	    			next_level.append(node.right)

	    	# now node is the last from curr_level (which was previously next_level)
	    	rightside.append(node.val)




