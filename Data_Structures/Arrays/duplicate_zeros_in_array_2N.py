class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        possible_dupes =0 
        length_ = len(arr) - 1

        # find num of zeros to be duplicated (excluding leftmost if exists)
        for left in range(length_ +1):
            