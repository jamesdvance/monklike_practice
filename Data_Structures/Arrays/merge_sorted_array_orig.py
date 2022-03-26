class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n > 0:
            new_arr = [0]*(m+n)
            nums1a = nums1.copy()
            iter_range = max([n,m])

            if iter_range ==m:
                longest="m"
            else:
                longest="n"

        
            
            if nums1a[0] < nums2[0]:
                first = nums1a[0]
                second = nums2[0]
            else:
                first =nums1a[0]
                second = nums2[0]

            nums1[0] = first
            nums1[1] = second
            idx_tup = (0, 1)
            val_tup = (first ,second)
            compare_range = min([n,m])
            if m+n >1:
                for i in range(1, iter_range):
                    if i < compare_range:
                        if nums2[i] < nums1a[i]:
                            first = nums2[i]
                            second = nums1a[i]
                        else:
                            second = nums2[i]
                            first = nums1a[i]

                        if first > val_tup[1]:
                            nums1[2*i] = first
                            nums1[(2*i)+1] = second
                            val_up = (first,second)

                        elif second < val_tup[0]:
                            nums1[idx_tup][0] = first
                            nums1[idx_tup[1]] = second
                            nums1[2*i] = val_tup[0]
                            nums1[(2*i)+1] = val_tup[1]

                        elif first > val_tup[0]:
                            if second > val_tup[1]:
                                nums1[idx_tup[1]] = first
                                nums1[2*i] = val_tup[1]
                                nums1[(2*i)+1] = second
                                val_tup = (val_tup[1],second)
                            else:
                                nums1[idx_tup[1]] = first
                                nums1[2*i] = second
                                nums1[(2*i)+1] =val_tup[1]
                                val_tup = (second, val_tup[1])                        


                        idx_tup = (2*i, (2*i)+1)

                    else:
                        print("got to over time")
                        if longest=="m":
                            first = nums1a[i]
                        else:
                            first = nums2[i]

                        nums1[(2*compare_range)+(i-compare_range)] = first
        print(nums1)