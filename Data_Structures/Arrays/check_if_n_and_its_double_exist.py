class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        """
        Thoughts
            1. arr is at least size 2
            2. no restriction on space
            3. The obvious case is linear search while checking against every previous val O(N^2) approx 
            4. Can use binary search by creating a seperate arr of 2N as we iterate 
            5. Will need to look for 2N and N/2
        """

        for i in range(len(arr)):
            oth_arr = list(arr)
            oth_arr.remove(arr[i])
            if 2*arr[i] in oth_arr:
                return True
            if arr[i]/2 in oth_arr:
                return True
                              
        return False