class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Thoughts:
            1. Seems to make sense to iterate right to left
            2. Keep a counter of the max elem.continue to write it, until you encounter the next max elem
            3. Start with -1
        """

        max_el = -1
        for i in range(len(arr)-1,-1,-1):
            elem = arr[i]
            arr[i] = max_el
            if elem > max_el:
                max_el = elem 

        return arr