"""
1. Find difference of two arrays
"""

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(set(nums1)-set(nums2)), list(set(nums2)-set(nums1))]

"""
2. Minimum deletions to make array beautiful
Array is beautiful if:
1. nums.length is even.
2. nums[i] != nums[i + 1] for all i % 2 == 0.
"""

class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        """
        Approach:
        1. Need to iteratively check conditions 
        2. Can't verify second conditino without iterating through whole array or nearly
        3. Knowing how many evens where nums[i] == nums[i+1] will tell me how many deletions needed
        and then can check for an additional deletion to make length even
        4. Will then need to solve the case where the next # is also even. Oh well
        5. And, if we delete one, then the other cases may become odd and won't have to delete
        """
        if nums == []:
            return 0

        del_total =0
        n = len(nums)
        i=0
        while i < n-1-del_total:
            if i%2 ==0:
                if nums[i] == nums[i+1]:
                    nums.pop(i)
                    del_total+=1
                else:
                    i+=1

            else:
                i+=1

        if len(nums)%2 != 0:
            del_total+=1

        return del_total

"""
3. Find Palimdrome with fixed length

Given an integer array queries and a positive integer intLength, 
return an array answer where answer[i] is either the queries[i]th 
smallest positive palindrome of length intLength or -1 if no such palindrome exists.

A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.
"""
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        """
        Approach:
        1. Need to calculate as many palindromes that can exist
        2. How to calculate a palindrome. If it can't have leading zeros, the smallest always seems to be 1(0*n-2)1 etc
        3. Need some rules on calculating a palindrome and then on calculating max palindrome at length. E.g. no more than 10
        2-digit palindromes. 

        the 5th length 3 would be 201
        """
        max_pal = (intLength-1)*10

        ret_arr = []
        for num in queries:
            if num > max_pal:
                ret_arr.append(-1)
            elif num%2!=0:
                ret_arr.append((num-1)+10**(intLength/2))
            else:
                ret_arr.append((num-1)+10**(intLength/2-1))

        return ret_arr

"""
4. Max Value of K coins from piles

There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the 
composition of the ith pile from top to bottom, and a positive integer k, 
return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.
"""

class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        """
        Approach:
        1. Practically need to create some kind of tree
        2. Is a shortest possible path between each node almost
        3. Can create running tallys of path value while iterating through each list
            Can continue iterating until k
            Can't use a agreedy approach because opt path may not be greedy
        """






