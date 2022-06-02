"""
Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. 
Each element in the result must be unique and you may return the result in any order.

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

1 <= nums1.length, nums2.length <= 1000

Rephrase: return an array of all unique elements shared between nums1 and num2

Inputs: two integer lists. Outputs: 1 integer list

Examples: [1,2,2], [2,2]; [3,4], [6,5]

Data structures:
New list to hold unique elems (sorted ascending) to return
New set to hold all unique elems seen but not matched
new set to hold all unique elems already added

Seems trivial to do in n+m time. 

Pseudo:

for i in longer_arr:
    if longer_arr[i] not in existing_set:
        add_to_existing_set 

for j in shorter_arr:
    if shorter_arr[j] in existing_set:
        add_to_return_set

Example:
[1,2,2]; [2,2]
existing_set = (1,2)
return_list = [2]

Example: [3,4], [6,5]
existing_set = (3,4)
return_list = ()
"""
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        n1,n2 = len(nums1), len(nums2)
        min_arr = nums1 if n1 <= n2 else nums2 
        max_arr = nums2 if n1 <=n2 else nums1 
        del nums1, nums2, n1, n2

        existing_set = set()
        return_list= set()
        for i in max_arr:
            if i not in existing_set:
                existing_set.add(i)

        for j in min_arr:
            if j in existing_set and j not in return_list:
                return_list.add(j)

        return list(return_list)

"""
Leetcode 2 set way (same as mine but quicker)
"""
class Solution:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2,set1)


"""
Leetcode smartass way (build in intersection)
"""

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1.intersection(set2))
        # or return list(set1 & set2)