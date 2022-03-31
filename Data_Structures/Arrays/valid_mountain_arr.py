class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        """
        Approach
            1. Iterate through, tracking prev
            2. If 
        """

        if len(arr) < 3:
            return False

        downslope=False

        if arr[1] <= arr[0]:
            return False 

        for i in range(2, len(arr)): # can't get to downslope on last one

            if arr[i-1] > arr[i] and not downslope:
                if i == len(arr)-1:
                    return False
                downslope= True

            elif arr[i-1] < arr[i] and downslope:
                return False 

            elif arr[i-1] == arr[i]:
                return False

        return downslope