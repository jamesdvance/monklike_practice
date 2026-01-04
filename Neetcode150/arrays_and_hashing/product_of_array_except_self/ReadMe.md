# Product of Array Except Self

## Summary

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all elements of `nums` except `nums[i]`. You must solve it without using division and in O(n) time.

### Key Points
- Cannot use division (handles zeros elegantly)
- Use prefix and suffix products
- The product at each index = product of all elements to the left * product of all elements to the right

### Optimal Approach
Calculate prefix products (left to right), then multiply by suffix products (right to left).

```python
def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    result = [1] * n

    # Calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Multiply by suffix products
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result
```

### Complexity
- Time: O(n) - two passes through the array
- Space: O(1) - excluding the output array (only using a single variable for running product)

---

## Detailed Explanation

### Problem Analysis

The naive approach would multiply all elements then divide by each element, but this fails when zeros are present and violates the no-division constraint. The insight is that for each position, we need the product of two independent ranges: everything before and everything after.

### Understanding Prefix and Suffix Products

For array `[a, b, c, d]`:
- Prefix products: `[1, a, ab, abc]` (product of all elements before index i)
- Suffix products: `[bcd, cd, d, 1]` (product of all elements after index i)
- Result: `[bcd, acd, abd, abc]` (prefix[i] * suffix[i])

### Step-by-Step Example

For `nums = [1, 2, 3, 4]`:

After prefix pass:
- result[0] = 1 (nothing before)
- result[1] = 1 (prefix so far)
- result[2] = 1 * 2 = 2
- result[3] = 1 * 2 * 3 = 6

After suffix pass (multiplying):
- result[3] = 6 * 1 = 6
- result[2] = 2 * 4 = 8
- result[1] = 1 * 12 = 12
- result[0] = 1 * 24 = 24

Final result: `[24, 12, 8, 6]`

### Alternative: Two Separate Arrays

A clearer but more space-intensive version:

```python
def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n

    for i in range(1, n):
        prefix[i] = prefix[i-1] * nums[i-1]

    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i+1] * nums[i+1]

    return [prefix[i] * suffix[i] for i in range(n)]
```

- Space: O(n) for the two auxiliary arrays

### Handling Zeros

The prefix/suffix approach handles zeros naturally:
- If there is one zero, all positions except the zero's position will be zero
- If there are multiple zeros, all positions will be zero
- The position with zero gets the product of all other elements

### Edge Cases
- Array with a single zero: only the zero's position has a non-zero result
- Array with multiple zeros: all results are zero
- Array of length 2: straightforward swap
- Large products: may cause integer overflow in some languages (not an issue in Python)

### Why No Division?

The no-division constraint:
1. Avoids division by zero errors
2. Makes the solution work uniformly regardless of zeros
3. Tests understanding of prefix/suffix decomposition

### Related Problems
- Maximum Product Subarray: finding contiguous subarray with maximum product
- Trapping Rain Water: similar prefix/suffix pattern
- Subarray Sum Equals K: prefix sum variant
