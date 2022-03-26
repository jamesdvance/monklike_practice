class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Options
        1. Write nums2 to last n digits of nums2 and sort array O(nlogn)
        2. Iterate through nums1 and nums2 simultaneously and when find a slot for an n num, move whole array forward O(nlogn)
        3. Write nums2 to last n digits of nums1 and swap nums1 for nums2
        4. Iterate in reversed order m to 0 and n to 0, putting either m or n at the end of the array and then stopping O(m+n)
        """

        while m>0 and n > 0:
            # TODO - fix the n-index
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                nums1[m-1] =0 # unnecessary but helpful marker
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1

        if n > 0:
            nums1[0:n] = nums2[0:n]

