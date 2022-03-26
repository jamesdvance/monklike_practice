class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Looking for O[N] time. So going to be looser with space
        1. Obviously, we only need to sort, aka, replace negative numbers
        2. Could cycle through the array, creating a new stack of negative numbers
        3. As you find a number larger than the abs val of the last item in the stack, pop it out
        4. Treat numbers >= 0 as a seperate array
        5. Create an empty array 
        """
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if nums[0] >=0:
            return [num**2 for num in nums]

        nums_len = len(nums)
        neg_end = -1
        # Find breakpoint
        for i in range(nums_len):
            if nums[i] >= 0:
                neg_end = i-1
                break
                
        if neg_end == -1:
            new_arr = [num**2 for num in nums]
            new_arr.reverse()
            return new_arr

        new_arr = list()
        j = neg_end+1
        for i in reversed(range(neg_end+1)):
            
            n2 = nums[i]**2
            if j < nums_len:
                p2 = nums[j]**2
                while p2 < n2 and j < nums_len:
                    new_arr.append(p2)
                    j+=1
                    if j == nums_len:
                        break
                        
                    p2 = nums[j]**2
                    
                new_arr.append(n2)

            else:
                new_arr.append(n2) 

        if j < nums_len:
            new_arr = new_arr + [num**2 for num in nums[j:len(nums)]]

        return new_arr



        return nums