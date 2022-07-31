"""
Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Approach: Use a hashmap to lookup the non-zero indexes
"""

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = {}
        for i,num in enumerate(nums):
        	if num:
        		self.nonzeros[i]=num 

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        l1 = len(vec.nonzeros)
        l2 = len(self.nonzeros)
        def sum_prod(dict1, dict2):
        	return sum([val * dict2.get(key, 0) for key, val in dict1.items()])

        if l2 < l1:
        	return sum_prod(vec.nonzeros, self.nonzeros)
        else:
        	return sum_prod(self.nonzeros, vec.nonzeros)

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)


"""
Approach2 : No hashmap
"""

class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = []
        for i,num in enumerate(nums):
        	if num:
        		self.nonzeros.append((i,num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        l1 = len(vec.nonzeros)-1
        l2 = len(self.nonzeros)-1
        def sum_prod(list1,list2):
        	i1,i2=0,0
        	final_prod=0
        	while i1 < len(list1) and i2 < len(list2):
        		if list1[i1][0] < list2[i2][0]:
        			i1+=1 
        		elif list1[i1][0] > list2[i2][0]:
        			i2+=1
        		else:
        			final_prod+=list1[i1][1]*list2[i2][1]
        			i1+=1
        			i2+=1

        	return final_prod

        if l2 < l1:
        	return sum_prod(vec.nonzeros, self.nonzeros)
        else:
        	return sum_prod(self.nonzeros, vec.nonzeros)

"""
Approach3 : No hashmap with binary search
"""


class SparseVector:
    def __init__(self, nums: List[int]):
        self.nonzeros = []
        for i,num in enumerate(nums):
        	if num:
        		self.nonzeros.append((i,num))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        l1 = len(vec.nonzeros)-1
        l2 = len(self.nonzeros)-1
        def sum_prod(list1,list2):
        	i1,i2=0,0
        	final_prod=0
        	while i1 < len(list1) and i2 < len(list2):
        		if list1[i1][0] < list2[i2][0]:
        			i1+=1 
        		elif list1[i1][0] > list2[i2][0]:
        			i2+=1
        		else:
        			final_prod+=list1[i1][1]*list2[i2][1]
        			i1+=1
        			i2+=1

        	return final_prod

        if l2 < l1:
        	return sum_prod(vec.nonzeros, self.nonzeros)
        else:
        	return sum_prod(self.nonzeros, vec.nonzeros)


    def search(i, arr):
    	l, r = 0, len(arr)-1
    	while l <= r:
    		m = (l+r)//2
    		if arr[mid][0]==i:
    			
