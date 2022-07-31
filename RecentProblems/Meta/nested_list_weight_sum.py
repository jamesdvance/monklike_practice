"""
339. Nested List Weight Sum
Medium

1374

313

Add to List

Share
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists.

The depth of an integer is the number of lists that it is inside of. For example, the nested list [1,[2,2],[[3],2],1] has each integer's value set to its depth.

Return the sum of each integer in nestedList multiplied by its depth.

 

Example 1:


Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
Example 2:


Input: nestedList = [1,[4,[6]]]
Output: 27
Explanation: One 1 at depth 1, one 4 at depth 2, and one 6 at depth 3. 1*1 + 4*2 + 6*3 = 27.
Example 3:

Input: nestedList = [0]
Output: 0

Approach: 
DFS using a recursive stack and keeping track of the nth nesting
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        

        def dfs(nested, lvl) -> int:

        	total = 0 

        	for item in nested:
        		if item.isInteger():
        			total+=lvl * item.getInteger() 
        		else:
        			total += dfs(item.getList(), lvl+1)

        	return total 

        return dfs(nestedList, 1 )

"""
BFS Solution

This was my solution
An alternative to popping and appending a full list is to iterate over the length of the entire q each cycle
That way things that get appended aren't included in that iteration
"""
from collections import deque
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
    	lvl = 0
    	q = deque([[nestedList]])
    	total =0 
    	while q:
    		cur_list = q.popleft()
    		lvl+=1
    		new_list = []
    		for nest_list in cur_list:
    			for item in nest_list:
	    			if item.isInteger():
	    				total+=lvl*item.getInteger()
	    			else:
	    				new_list.append(item.getList())

    		if new_list:
    			q.append(new_list)

    	return total

    		



