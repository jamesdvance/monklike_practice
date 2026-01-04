# Time Based Key-Value Store

## Summary

Design a time-based key-value data structure that can store multiple values for the same key at different timestamps and retrieve the value for a key at a given timestamp.

### Key Points
- Store (value, timestamp) pairs for each key
- Timestamps are strictly increasing for each key
- Use binary search to find the largest timestamp <= given timestamp

### Optimal Approach
Use a dictionary mapping keys to lists of (timestamp, value) pairs. Binary search to find the appropriate value.

```python
from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        # Binary search for rightmost timestamp <= given timestamp
        idx = bisect.bisect_right(values, (timestamp, chr(127)))

        if idx == 0:
            return ""

        return values[idx - 1][1]
```

### Complexity
- set: O(1) amortized
- get: O(log n) where n is number of values for that key
- Space: O(total number of set operations)

---

## Detailed Explanation

### Problem Analysis

This is a design problem that combines hash maps with binary search. The key insight is that timestamps are strictly increasing, so values for each key form a sorted list by timestamp. This enables efficient binary search for queries.

### The Get Operation

For get(key, timestamp), we need:
- The value with the largest timestamp that is <= the given timestamp
- If no such timestamp exists, return ""

This is a "find rightmost element <= target" binary search problem.

### Why bisect_right with (timestamp, chr(127))?

When using bisect on (timestamp, value) tuples:
- bisect_right finds the insertion point after all existing elements
- Using chr(127) (a high ASCII character) ensures we find the position after any value with the same timestamp
- Then idx - 1 gives us the rightmost element with timestamp <= given timestamp

Alternative without the chr(127) trick:

```python
def get(self, key: str, timestamp: int) -> str:
    if key not in self.store:
        return ""

    values = self.store[key]
    left, right = 0, len(values) - 1
    result = ""

    while left <= right:
        mid = (left + right) // 2
        if values[mid][0] <= timestamp:
            result = values[mid][1]
            left = mid + 1
        else:
            right = mid - 1

    return result
```

### Manual Binary Search Implementation

```python
class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""

        values = self.store[key]
        left, right = 0, len(values) - 1

        while left <= right:
            mid = (left + right) // 2

            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        # right is now the largest index with timestamp < given timestamp
        return values[right][1] if right >= 0 else ""
```

### Optimization: Store Separately

Store timestamps and values in separate lists for cache efficiency:

```python
class TimeMap:
    def __init__(self):
        self.timestamps = defaultdict(list)
        self.values = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timestamps[key].append(timestamp)
        self.values[key].append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""

        idx = bisect.bisect_right(self.timestamps[key], timestamp)

        if idx == 0:
            return ""

        return self.values[key][idx - 1]
```

### Edge Cases
- Key does not exist: return ""
- Timestamp smaller than all stored timestamps: return ""
- Exact timestamp match: return that value
- Timestamp between stored values: return the one just before

### Real-World Applications

Time-based key-value stores are used in:
- Version control systems (git objects by commit time)
- Database temporal queries
- Caching with TTL
- Event sourcing systems

### Related Problems
- Design Underground System: similar time-based tracking
- Stock Price Fluctuation: track prices over time
- Snapshot Array: versioned array
