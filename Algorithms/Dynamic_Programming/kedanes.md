# Kedane's Algorithm for 1-D Dynamic Programming

## Common Use
Commonly used to solve a maximum subarray problem. The largest possible sum of a contiguous subarray of a 1-D array with negative numbers. 

## Steps
1. Initialize array dp of length of original array
2. Iterate over length of original array. At each step, set dp[i] to the max of arr[i] and dp[i-1] + arr[i]

