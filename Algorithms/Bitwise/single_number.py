"""
My silly arbitrary solution
O(N) time
O(N) space (worst case)
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = {}
        
        for num in nums:
            counts[num] = 1+counts.get(num,0)
            if counts[num]==2:
                del counts[num]
                
        return list(counts.keys())[0]

"""
Better 
"""
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = set()
        
        for num in nums:
            if num in counts:
            	counts.remove(num)
            else:
            	counts.add(num)
                
        return counts[0]

"""
Bitwise solution

O(N) time
O(1) space

Uses binary operation called XOR

For example: 

[2,2,1]
2 in binary is 010. 
010 & 010 = 000
So ever other 010

^ is the XOR operator in python


"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    	a=0
    	for num in nums:
    		a^= num

    	return nums