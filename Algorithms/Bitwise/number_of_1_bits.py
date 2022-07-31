"""
Constant time O(32) solution
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n: # while n > 0
            res += n % 2 # only 1 if n % 2 ==1, aka if 1
            n = n>>1 # shift bits to the right. The rightmost point is the final one's place

        return res


"""
Constant time O(num bits) solution
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        res =0
        while n:
            n = n & (n-1)
            res+=1

        return res