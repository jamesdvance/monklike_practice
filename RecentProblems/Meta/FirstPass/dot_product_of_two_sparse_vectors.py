"""
1570. Dot Product of Two Sparse Vectors

Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

 

Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
Example 2:

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
Example 3:

Input: nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]
Output: 6

Two Pointer Technique
"""

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums_map = []
        for i, v in enumerate(nums):
        	if v != 0:
        		self.nums_map.append((i,v))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
    	i = j = 0
    	ret_sum = 0
    	vec_map = vec.nums_map
    	while i< len(self.nums_map) and j < len(vec_map):
    		if self.nums_map[i][0] < vec_map[j][0]:
    			i+=1 
    		elif self.nums_map[i][0]>vec_map[j][0]:
    			j+=1
    		else:
    			ret_sum+=self.nums_map[i][1]*vec_map[j][1]
    			i+=1 
    			j+=1 

    	return ret_sum


"""
Binary Search
"""

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums_map = []
        for i, v in enumerate(nums):
        	if v != 0:
        		self.nums_map.append((i,v))
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
    	ret_sum = 0
    	vec_map = vec.nums_map
    	if len(vec_map) > len(self.nums_map):
    		shorter, longer = self.nums_map, vec_map
    	else:
    		longer, shorter = vec_map, self.nums_map

    	j = 0
    	for idx, val in shorter:
    		long_idx, long_val,list_idx = self.binary_search(longer[j:], idx)
    		if long_idx != -1:
    			ret_sum+= long_val*val 
    			j = list_idx+1

    	return ret_sum


    def binary_search(self, arr, n)->tuple:
    	"""
		Returns tuple
    	"""
    	l, r = 0, len(arr)-1

    	while l <= r: 
    		mid = (l+r)//2
    		if arr[mid][0]==n:
    			return arr[mid] 

    		elif arr[mid][0] < n:
    			l = mid+1 
    		else:
    			r = mid-1 

    	return (-1,0, mid)