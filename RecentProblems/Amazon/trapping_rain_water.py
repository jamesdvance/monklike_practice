"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Input: height = [4,2,0,3,2,5]
Output: 9
"""

"""
Two Pointer Approach
"""

class Solution:
    def trap(self, height: List[int]) -> int:

    	l, r=0, len(height)-1
    	l_max, r_max =height[0], height[-1]
    	res = 0
    	while l < r: 

    		if height[l] < height[r]:
    			if height[l] >= l_max:
    				l_max = height[l]
    			else:
    				res+=l_max-height[l]
    			l+=1
    		else:
    			if height[r] >= r_max:
    				r_max = height[r ]
    			else:
    				res+=r_max - height[r]
    			r-=1

    	return res 
"""
DP Approch
"""

class Solution:
    def trap(self, height: List[int]) -> int:
    	res =0
    	h = len(height)
    	left_max =[0]*h 
    	right_max = [0]*h 
    	left_max[0] = height[0]
    	right_max[-1]=height[-1]
    	# iterate over h, finding left max
    	for i in range(1,h):
    		left_max[i] = max(height[i],left_max[i-1]) # Kadane's basically 

    	# Iterate over h, finding right max
    	for i in range(h-2, -1,-1):
    		right_max[i] = max(height[i],right_max[i+1])

    	# You now how have the highest right and left at this i. Water can reach the lowest of the both max's
    	# Leave out the two ends, as they will never count
    	for i in range(1, h-1):
    		res+=min(left_max[i],right_max[i])-height[i]

    	return res

"""
Stack Approach

Don't like how it calculates distance
"""

class Solution:
    def trap(self, height: List[int]) -> int:
    	stack = []
    	res = 0
    	i =0 
    	while i < len(height):
    		while stack and height[i] > height[stack[-1]]:
    			top = stack.pop()
    			if not stack:
    				break 
    			dist = i - stack[-1] -1 
    			bounded_height = min(height[i], height[stack[-1]]- height[top])
    			res+=dist+bounded_height 

    		i+=1 
    		stack.append(i)

    	return res 

