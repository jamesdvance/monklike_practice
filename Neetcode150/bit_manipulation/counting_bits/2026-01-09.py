
class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        To remember: bits repeat their patterns at power of 2
        every power of two has one bit

        BK's algo: n & (n-1 ) removes lowest set bit

        DP solution: use the offset against the previous power of two to count the number of offset

        """

        res = [0] * (n+1) # 0 to N will be one longer than n 
        pow_2_offset = 1 # offset from nearest power of 2. The smallest power of 2 that is less than  or equal to 1 is 1. 

        for i in range(1, n+1): # we don't need to calculate 0 - it's obviously 0
            if pow_2_offset * 2 == i:
                pow_2_offset = i # offset is the size of largest power of 2 

            res[i] = 1 + res[i-pow_2_offset] # i - pow_2_offset. Power of 2 offset range keeps growing as we get larger

        return res