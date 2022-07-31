"""

Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.


"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ret_sum=0
        roll_sum=0
        sums= {0:1}
        for num in nums:
            roll_sum+=num
            diff = roll_sum-k 
            if diff in sums:
                ret_sum+=sums[diff]
            sums[roll_sum]  = sums.get(roll_sum,0) + 1 

        return ret_sum

