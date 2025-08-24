from typing import List
def prefix_sum(arr:List[int]):

    prefix_arr = [arr[0]]
    for i in range(1, len(arr)):
        prefix_arr.append(prefix_arr[-1]+arr[i])

    return prefix_arr