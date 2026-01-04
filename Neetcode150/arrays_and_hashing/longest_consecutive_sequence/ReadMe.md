# Longest Consecutive Sequence

## Summary

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence. The algorithm must run in O(n) time.

### Key Points
- Cannot sort (that would be O(n log n))
- Use a hash set for O(1) lookups
- Only start counting from sequence beginnings (numbers with no predecessor)

### Optimal Approach
Add all numbers to a set. For each number, if it has no predecessor (num-1 not in set), count the consecutive sequence starting from it.

```python
def longestConsecutive(nums: list[int]) -> int:
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start from sequence beginning
        if num - 1 not in num_set:
            current = num
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest
```

### Complexity
- Time: O(n) - each number is visited at most twice
- Space: O(n) - hash set stores all numbers

---

## Detailed Explanation

### Problem Analysis

The O(n) time constraint eliminates sorting as an option. The key insight is that we can use a hash set to check for consecutive numbers in O(1) time. The clever optimization is to only start counting from numbers that are the beginning of a sequence.

### Why This is O(n)

At first glance, the nested loops might suggest O(n^2), but each number is processed at most twice:
1. Once when added to the set
2. Once when counted as part of a sequence

Numbers that are not sequence starts are skipped in the outer loop but counted in some inner while loop. Numbers that are sequence starts initiate a count. The total work across all while loops is O(n).

### Step-by-Step Example

For `nums = [100, 4, 200, 1, 3, 2]`:

Set: {100, 4, 200, 1, 3, 2}

- num = 100: 99 not in set, so start here. 101 not in set. Length = 1
- num = 4: 3 is in set, skip (not a sequence start)
- num = 200: 199 not in set, so start here. 201 not in set. Length = 1
- num = 1: 0 not in set, so start here. Count 1, 2, 3, 4. Length = 4
- num = 3: 2 is in set, skip
- num = 2: 1 is in set, skip

Longest = 4

### Alternative: Union-Find Approach

Use Union-Find to merge consecutive numbers:

```python
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.size = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.size[x] = 1
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.size[px] < self.size[py]:
                px, py = py, px
            self.parent[py] = px
            self.size[px] += self.size[py]

def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    uf = UnionFind()
    num_set = set(nums)

    for num in nums:
        uf.find(num)  # Initialize
        if num + 1 in num_set:
            uf.union(num, num + 1)

    return max(uf.size.values()) if uf.size else 0
```

This is more complex but demonstrates an alternative technique.

### Sorting Approach (O(n log n))

If the O(n) constraint were relaxed:

```python
def longestConsecutive(nums: list[int]) -> int:
    if not nums:
        return 0

    nums = sorted(set(nums))
    longest = 1
    current = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] + 1:
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    return longest
```

### Edge Cases
- Empty array: return 0
- Single element: return 1
- All duplicates: return 1
- All consecutive: return n
- Negative numbers: handled normally
- Large gaps between sequences: each sequence counted independently

### Common Mistakes
- Forgetting to handle duplicates (use a set)
- Not checking for sequence starts, leading to O(n^2)
- Off-by-one errors in sequence counting

### Related Problems
- Binary Tree Longest Consecutive Sequence: tree variant
- Longest Increasing Subsequence: different constraint (not necessarily consecutive values)
- Array Nesting: similar "follow the chain" pattern
