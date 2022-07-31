"""
1570. Dot Product of Two Sparse Vectors

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector 
efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8


Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0

Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6

Rephrase: Initialize sparse vector and return dot product with another sparse vector

Data structures: 
hashmap where the key is the index a value, and the value is the value

That would be stupid simple. 
It is stupid simple. From the comments, turns out hash maps are complex to computationally implement
"""

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums_map = {i:nums[i] for i in range(len(nums)) if nums[i] !=0}
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        # one optimization: Choose the smaller of the two arrays to iterate over
        return sum([vec.nums_map.get(k,0)*v for k,v in self.nums_map.items()])
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)

"""
Here's a solution that would include resolve the complexity from hashing: Index-value pairs
"""
class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = [] 
        for i, val in enumerate(nums):
            if val !=0:
                self.pairs.append([i, val])

    def dotProduct(self,vec:'SparseVector') -> int:
        result = 0
        p,q = 0,0 # initialize two pointers. Iterate through both pairs. Remember, both are sorted
        while p < len(self.pairs) and q < len(vec):
            if self.pairs[p][0] == vec[q][0]:
                result += self.pairs[p][1] * vec[q][1]
                q +=1
                p+=1
            elif self.pairs[p][0] < vec[q][0]:
                p+=1 
            else:
                q+=1 

        return result
