class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        just_duped = False
        for i in range(len(arr)-1):
            
            if just_duped == True:
                just_duped = False
                continue
                
            if arr[i] ==0:
                next_one = arr[i+1]
                for j in range(i+1,len(arr)-1):
                    next_next = arr[j+1]
                    arr[j+1] = next_one
                    next_one = next_next
                
                arr[i+1] = 0
                just_duped = True