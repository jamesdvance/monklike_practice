"""
4. Median of Two Sorted Arrays
Hard

17412

2085

Add to List

Share
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
Accepted
1,446,788
Submissions
4,201,777
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    	A, B = nums1, nums2 
    	if len(A) < len(B):
    		B,A = nums1, nums2 

    	# Full length
    	N = len(A) + len(B) 
    	l,r = 0, N-1
    	half=N//2

    	# Aim is to find single point in A and B that represent the n, n-1 partition point
    	while True:
    		i =(l+r)//2
    		j = half-i - 2 # index of remainder - partition that exists in B 

    		Aleft = A[i] if i>=0 else float("-infinity")
    		Aright = A[i+1] if i < N-1 else float("infinity")
    		Bleft = B[i] if i >=0 else float("-infinity")
    		Bright = B[i+1] if i < N-1 else float("infinity")

    		if Aleft <= Bright and Bleft <= Aright: 

    			if N % 2 ==0:
    				return min(Aright, Bright)

    			else:
    				return (max(Aleft, Bleft) + min(Aright,Bright))/2

    		elif Aleft > Bright:
    			r = i -1 
    		else:
    			l = i +1 