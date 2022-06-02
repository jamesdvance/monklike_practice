"""
  First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check.
 Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Input: n = 1, bad = 1
Output: 1

1 <= bad <= n <= 231 - 1

Rephrase: Find the minimum index from 1 to n that returns True. There will always be at least one that returns True

Inputs: n: integer. returns integer index (from 1 to n!)

examples: n=5, bad =4, n=5,bad =1, n=1,bad=1

Data structures:
start, end, mid (binary search)

pseudo:

calc_mid
if mid and (mid ==1 or not mid-1):
    return mid
if mid: # implied (and mid-1)
    end = mid-1
else:
    start = mid+1


Examples: n=5, bad=4
start =1, end = 5, mid=3
start = 4, end=5, mid=4
return 4

n=5, bad=1
start = 1, end =5, mid =3
start = 1, end = 4, mid =2
start = 1, end =1, mid =1
return 1


"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n 

        # further minimize api calls
        # called = {}

        while start <=end:
            mid = (end+start)//2
            mid_bool = isBadVersion(mid)
            if mid_bool and (mid==1 or not isBadVersion(mid-1)):
                return mid 
            if mid_bool:
                end = mid-1 
            else:
                start = mid+1

        return (end+start)//2 # catches case of len 1