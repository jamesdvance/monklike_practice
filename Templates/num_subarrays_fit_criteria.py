from collections import defaultdict

def num_subbarrays(arr: list, k:int):
    """
    Subarrays of size k that fit criteria
    """
    ans = curr = 0

    counts = defaultdict(int)
    counts[0] = 1 

    for num in arr:
        ans+= counts[num-k]
        counts[curr] += 1 



