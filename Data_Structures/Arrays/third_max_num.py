
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        Given an integer array nums, return the third distinct maximum 
        number in this array. If the third maximum does not exist, return the maximum number.

        Approach:
        Base case: sort set of the array, and find 3rd from last

        O(N) approach:
        1. Iterate through the arra, 
        """

        # Here's the simple base case
        unq_nums = list(set(nums))
        if len(unq_nums) >2:
            unq_nums.sort(reverse=True)
            return unq_nums[2]
        
        else:
            return max(unq_nums)


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        Trying for O(N) case:
        1. We can't sort
        2. Will need to track max in a way allows backwards-comparison

        greater = []
        lesser = []
        Anytime there is a max, it becomes the new pivot
        We keep track of all of the old pivots
        
        """

        # 
        if len(set(nums))<3:
            return max(nums)
               
        first_max, second_max, third_max =-2**32,-2**32,-2**32

        for num in nums:
            if num == first_max or num == second_max or num == third_max:
                continue
                
            if num > first_max:
                third_max = second_max
                second_max = first_max 
                first_max = num 

            elif num > second_max and num < first_max:
                third_max = second_max
                second_max = num 

            elif num > third_max and num <second_max:
                third_max = num 


        return third_max


"""
Leetcode's O(N) Solution 1: Delete first two maximums from a set
"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        # Make a Set with the input.
        nums = set(nums)

        # Find the maximum.
        maximum = max(nums)

        # Check whether or not this is a case where
        # we need to return the *maximum*.
        if len(nums) < 3:
            return maximum

        # Otherwise, continue on to finding the third maximum.
        nums.remove(maximum)
        second_maximum = max(nums)
        nums.remove(second_maximum)
        return max(nums)

"""
Leetcode's O(N) Solution 2: Keep a set of seen maximums

1. Iterate through three times
2. Track a max each time,but don't let numbers already in seen_maximums be the max
3. Return the min of the set of seen maximums
"""

    def maximum_ignoring_seen_maximums(nums, seen_maximums):
        maximum = None
        for num in nums:
            if num in seen_maximums:
                continue
            if maximum == None or num > maximum:
                maximum = num
        return maximum

    seen_maximums = set()

    for _ in range(3):
        current_maximum = maximum_ignoring_seen_maximums(nums, seen_maximums)
        if current_maximum == None:
            return max(seen_maximums)
        seen_maximums.add(current_maximum)

    return min(seen_maximums)

"""
Leetcodes O(N) Solution 3: 3 Maximums using a set
1. Create set to hold max's
2. Iterate once through nums and keep adding to the maximums set. Then remove min elem once len gets greater than 3
"""
def thirdMax(self, nums: List[int]) -> int:
    maximums = set()
    for num in nums:
        maximums.add(num)
        if len(maximums) > 3:
            maximums.remove(min(maximums))
    if len(maximums) == 3:
        return min(maximums)
    return max(maximums)
