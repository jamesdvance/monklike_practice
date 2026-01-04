# Maximum Product Subarray

## Summary

Given an integer array, find the contiguous subarray with the largest product.

### Key Points
- Unlike sum, products can flip sign with negative numbers
- Track both maximum AND minimum at each position
- Minimum can become maximum when multiplied by negative

### Optimal Approach
Track running max and min products.

```python
def maxProduct(nums: list[int]) -> int:
    result = nums[0]
    curr_max = curr_min = 1

    for num in nums:
        if num < 0:
            curr_max, curr_min = curr_min, curr_max

        curr_max = max(num, curr_max * num)
        curr_min = min(num, curr_min * num)

        result = max(result, curr_max)

    return result
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

Unlike Maximum Subarray (sum), products behave differently:
- Negative * negative = positive (min can become max)
- Zero resets everything

We need to track both the maximum and minimum product ending at each position.

### Why Track Minimum?

```
nums = [2, 3, -2, 4]

At -2:
  max_so_far = 6 (from 2*3)
  After multiplying by -2: 6 * -2 = -12 (becomes min)

At 4:
  If we had kept min = -12
  -12 * 4 = -48 (still min)
  But max = 4 (fresh start)
```

### The Swap Trick

When we see a negative number:
- Old max will become smaller (negative * positive = negative)
- Old min will become larger (negative * negative = positive)

So we swap before computing.

### Alternative Without Swap

```python
def maxProduct(nums: list[int]) -> int:
    result = nums[0]
    curr_max = curr_min = 1

    for num in nums:
        temp_max = max(num, curr_max * num, curr_min * num)
        curr_min = min(num, curr_max * num, curr_min * num)
        curr_max = temp_max

        result = max(result, curr_max)

    return result
```

We consider all three options: start fresh, extend max, extend min.

### Full DP Array Approach

```python
def maxProduct(nums: list[int]) -> int:
    n = len(nums)
    max_dp = [0] * n
    min_dp = [0] * n

    max_dp[0] = min_dp[0] = nums[0]
    result = nums[0]

    for i in range(1, n):
        if nums[i] >= 0:
            max_dp[i] = max(nums[i], max_dp[i-1] * nums[i])
            min_dp[i] = min(nums[i], min_dp[i-1] * nums[i])
        else:
            max_dp[i] = max(nums[i], min_dp[i-1] * nums[i])
            min_dp[i] = min(nums[i], max_dp[i-1] * nums[i])

        result = max(result, max_dp[i])

    return result
```

### Step-by-Step Example

```
nums = [2, 3, -2, 4]

i=0 (num=2):
  curr_max = max(2, 1*2) = 2
  curr_min = min(2, 1*2) = 2
  result = 2

i=1 (num=3):
  curr_max = max(3, 2*3) = 6
  curr_min = min(3, 2*3) = 3
  result = 6

i=2 (num=-2):
  Swap: curr_max=3, curr_min=6
  curr_max = max(-2, 3*-2) = -2
  curr_min = min(-2, 6*-2) = -12
  result = 6

i=3 (num=4):
  curr_max = max(4, -2*4) = 4
  curr_min = min(4, -12*4) = -48
  result = 6

Answer: 6
```

### Handling Zeros

Zero resets the subarray. The formulas handle this:
- max(0, curr_max * 0) = 0 (fresh start)
- min(0, curr_min * 0) = 0 (fresh start)

### Two-Pass Approach

```python
def maxProduct(nums: list[int]) -> int:
    def max_product_one_direction(arr):
        result = arr[0]
        product = 1
        for num in arr:
            product *= num
            result = max(result, product)
            if product == 0:
                product = 1
        return result

    return max(max_product_one_direction(nums), max_product_one_direction(nums[::-1]))
```

If there are even negatives, one direction will capture max.
If odd negatives, the other direction captures a different portion.

### Edge Cases
- Single element: return that element
- All positive: return product of all
- Contains zero: resets subarray
- Two negatives: their product is positive

### Related Problems
- Maximum Subarray: sum instead of product
- Product of Array Except Self: related product problem
- Subarray Sum Equals K: subarray with target sum
