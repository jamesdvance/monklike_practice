class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        """
        A school is trying to take an annual photo of all the students. 
        The students are asked to stand in a single file line in non-decreasing order by height. 
        Let this ordering be represented by the integer array expected where expected[i] is the 
        expected height of the ith student in line.

        You are given an integer array heights representing the current order that the students 
        are standing in. Each heights[i] is the height of the ith student in line (0-indexed).

        Return the number of indices where heights[i] != expected[i].

        Assume its supposed to be a sorted array. Given indiceces where elems are out of place

        Thoughts:
        1. Quick answer: copy the array, sort it, then iterate through and check if each elem matches
        2. Even in cases of duplies its ok. O(2NlogN)
        3. 
        """

        heights_sorted = list(heights)
        heights_sorted.sort()

        mismatches = 0 
        for i in range(len(heights)):

            if heights[i] != heights_sorted[i]:
                mismatches+=1

        return mismatches