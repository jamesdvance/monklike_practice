class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Approach:
            * iterate once through array
            * each time you encounter a 1, start a tally
            * once you don't encounter a 1, check against max value and swap if new amt is larger
            * if array length is known, can terminate once we're as far away from end as max value
        """

        max_ones = 0
        cur_ones = 0
        for num in nums:
            if num ==1:
                cur_ones+=1
                
            else:
                if cur_ones > max_ones:
                    max_ones = cur_ones

                cur_ones =0
                    
        if cur_ones > max_ones:
            max_ones = cur_ones
                
        return max_ones