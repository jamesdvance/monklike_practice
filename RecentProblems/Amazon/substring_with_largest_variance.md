# Substring With Largest Variance
https://leetcode.com/problems/substring-with-largest-variance/discuss/2352585/Kadane's-Algorithm-(Python)-with-clear-analysis
https://leetcode.com/problems/substring-with-largest-variance/discuss/2038952/Python-2*26*N-(faster-than-26*25*N)

## Intuition
This is another 'subarrays' problem, not unlike 'sum of subarray ranges' and 'sum of total strength of wizards'
In this case, the problem requires a Counter data structure for each subarray, and the difference between the highest and lowest count. For ALL possible substrings
We only need to return the largest possible variance. 

We saw in sum of subarray ranges, that the given range over a subarrays was equal to the sum of all subarray maxes minus the sum of all subarray minimums
However, instead of an array of integers, we are incrementing counts of characters and keeping a running max and min

### Dynamic Programming
Seeks to solve complex problem by breaking into simpler subproblems, solving each only once, and storing their solutions so the next time a sub problem occurs,
one can action off of the already-computed value. 

### Kadane's Algorithm
Kadane's algorithm is specifically for maximum subarray problems. This looks for the largest possible sum of a contigous subarray. With negatives, this is tricky. 
1. Start from the last element. Calculate the sum of every possible subarray ending with the element A[n-1]. Then,calculate the sum of every possible subarary ending with 
A[n-2], a[n-3], etc until A[0]

Recurrance relation: local_max[i]=max(A[i], A[i]+local_max[i-1]) # start subarray at this value, or include this value and the value before

Time complexity is only O(N)

### Peudo-code Kadane's 

for i in 0->array_size
  local_max = max(array[i], array[i]+local_max)
  global_max = max(global_max, local_max)

### Adapting to this problem
Kadane's requires at least one negative to be worth anything. Otherwise, the max 'subarray' of an all positive array is just sum of the array







