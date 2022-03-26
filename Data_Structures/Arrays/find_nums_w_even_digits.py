class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """
        Probably don't want to just convert into a string and call the length

        """
        total_even = 0
        for num in nums:
            digits = 0
            while num >= 1:
                digits+=1
                num/=10
            if digits%2==0:
                total_even+=1
                
        return total_even