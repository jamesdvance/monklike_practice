class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Given an array nums of n integers where nums[i] is in the range [1, n], 
        return an array of all the integers in the range [1, n] that do not appear in nums.

        Follow up: Could you do it without extra space and in O(n) runtime? 
        You may assume the returned list does not count as extra space.

        Base Case:
        O(2N) time 
        O(3N) space
        """
        ret_list = []
        full_list = list(range(1,len(nums)+1))
        check_dict = dict(zip(full_list,[0]*len(nums)))
        ret_arr = []
        for num in nums:
            check_dict[num] +=1
            
        for num in full_list:
            if check_dict[num] ==0:
                ret_list.append(num)

        return ret_list


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Given an array nums of n integers where nums[i] is in the range [1, n], 
        return an array of all the integers in the range [1, n] that do not appear in nums.

        Follow up: Could you do it without extra space and in O(n) runtime? 
        You may assume the returned list does not count as extra space.

        O(1) space

        Approach:
        1. Can't sort the list and stay in O[1]
        2. The index can be used when iterating through
        3. But hard to avoid O(N**2) if circling through index
        4. Can use the order. Try to swap the number with the index
        5. When an array is sorted, its trivial
        """

        for i in range(len(nums)):
            num = nums[i]
            # Swap
            nums[i], nums[num+1] = nums[num+1], nums[i]

        popped=0
        for i in range(len(nums)):
            if nums[i] == i-1+popped:
                nums.pop(i)
                popped+=1

        return nums

"""
Leetcode O(N) time O(1) space solution:
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Works by marking numbers already seen as negative
        Is just really smart
        """

        for i in range(len(nums)):

            new_index= abs(nums[i])-1 # We're creating an index based on the number. Use abs in case it was already 
                # turned negative

            if nums[new_index] >0: # don't want to keep flipping it pos and neg
                nums[new_index] *= -1 # 

        result = []
        for i in range(1, len(nums)+1): # iterate through the given index and check if its 
            if nums[i-1] > 0:
                result.append(i)

        return result


"""
Swapping solution from LeetCode comment
"""
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Makes the swap solution I was working on work.
        ... I don't see how the swap works completely.
        """
        for i in range(len(nums)):
            idx = nums[i] -1 #get the index of where this num should be

            while idx != nums[i]:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx = nums[i]-1

                if nums[i] == nums[idx]:
                    break

        result = []
        for i in range(1,len(nums)+1):
            if i-1 != nums[i]-1:
                result.add(i)


        return result

            


