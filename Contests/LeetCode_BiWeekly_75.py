"""
1. Minimum Bitflips To Convert Number
A bit flip of a number x is choosing a bit in the binary representation of x and
 flipping it from either 0 to 1 or 1 to 0.

For example, for x = 7, the binary representation is 111 and we 
may choose any bit (including any leading zeros not shown) and flip it. 
We can flip the first bit from the right to get 110, flip the second bit 
from the right to get 101, 
flip the fifth bit from the right (a leading zero) to get 10111, etc.
Given two integers start and goal, return the minimum number of 
bit flips to convert start to goal.

Thoughts:
1. Need a f't to derive bit str (with leading 0) from integer
2. Then probably a DP solution to find min # of changes
"""
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        def get_bit_str(q:int):
            bit_str =""
            while q >0:
                q, r = q//2, q%2
                bit_str+=str(r)
                
            return bit_str[::-1]

        start = get_bit_str(start)
        goal = get_bit_str(goal)
        while len(start) < len(goal):
            start = "0" + start
        while len(goal) < len(start):
            goal = "0" +goal

        dif =0
        i =0  
        while start != goal:
        	if start[i]!=goal[i]:
        		start = start[0:i]+goal[i]+start[i+1:len(start)]
        		dif +=1

        	i+=1

        return dif
         
"""
2. 6034. Find Triangular Sum of an Array
You are given a 0-indexed integer array nums, where nums[i] is a digit between 0 and 9 (inclusive).

The triangular sum of nums is the value of the only element present 
in nums after the following process terminates:

Let nums comprise of n elements. If n == 1, end the process. 
Otherwise, create a new 0-indexed integer array newNums of length n - 1.
For each index i, where 0 <= i < n - 1, assign the value of newNums[i] as 
(nums[i] + nums[i+1]) % 10, where % denotes modulo operator.
Replace the array nums with newNums.
Repeat the entire process starting from step 1.

Approach
"""

class Solution:
	def triangularSum(self, nums: List[int]) -> int:

		def getSum(nums)->list:
			n = len(nums)
			if n==1:
				return nums[0]
			else:
				new_nums = []
				for i in range(n-1):
					new_nums.append((nums[i]+nums[i+1])%10)

			return getSum(new_nums)

		return getSum(nums)


"""
3. 6035. Number of Ways to Select Buildings

You are given a 0-indexed binary string s which represents the types of buildings along a street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. 
However, to ensure variety, no two consecutive buildings out of the selected buildings 
can be of the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings 
as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.

Approach - isn't this just n choose k ? - no, its not about plain combinations
Sliding window approach seems to make sense
DP problem? Seems like we can never move the start slider forward
0 - 1 - 0 
1 - 
almost a tree
"""
class Solution:
    def numberOfWays(self, s: str) -> int:

    	i =0 # window start
    	j =0 # middle
    	k =0 # end
    	unq =0

    	one_dig = [] # queue
    	two_dig = [] # queue
    	
    	avail = []

    	for d in range(len(s)):
    		dig = s[d]
    		opp = "1" if dig =="0" else "0"

    		for e in range(len(s)):
    			if e < d -1 or e > d+1:
    				# non-neighbors
    				if s[e] != dig: 
    					
    		# Check all available and increment unq if qualify
    		# make own additions to available
    		if len(avail)==0:
    			avail.append({"next":opp, rem=2})

    		for a in range(len(avail)):
    			if avail.append(obj)



