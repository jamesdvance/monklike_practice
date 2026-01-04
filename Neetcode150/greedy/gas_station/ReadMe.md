# Gas Station

## Summary

There are n gas stations along a circular route. gas[i] is the gas at station i, cost[i] is the gas needed to travel to station i+1. Find the starting station to complete a circuit, or return -1 if impossible.

### Key Points
- If total gas >= total cost, a solution exists
- If we can't reach station i from start j, we can't reach i from any station between j and i
- Track current tank to find valid starting point

### Optimal Approach
Single pass with greedy reset.

```python
def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    total_tank = 0
    curr_tank = 0
    start = 0

    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        curr_tank += gas[i] - cost[i]

        if curr_tank < 0:
            start = i + 1
            curr_tank = 0

    return start if total_tank >= 0 else -1
```

### Complexity
- Time: O(n)
- Space: O(1)

---

## Detailed Explanation

### Problem Analysis

Two key insights:
1. If total(gas) >= total(cost), a solution exists
2. If starting from j we can't reach i, then starting from any station k (j < k <= i) also won't reach i

### Why the Second Insight?

If we fail at station i starting from j, our tank went negative. Any station k between j and i would have:
- Less or equal gas (we already used some getting from j to k)
- Same remaining cost to reach i

So k also fails at i (or earlier).

### The Algorithm

1. Try starting from station 0
2. If tank goes negative at station i, start over from i+1
3. After one pass, if total >= 0, the current start is valid

### Step-by-Step Example

```
gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

Net at each station: [-2, -2, -2, 3, 3]

i=0: curr=-2, start=1
i=1: curr=-2, start=2
i=2: curr=-2, start=3
i=3: curr=3
i=4: curr=3+3=6

total = -2-2-2+3+3 = 0 >= 0
start = 3

Verify: Start at 3 with tank=0
  Station 3: +4, tank=4, need 1 to reach 4, tank=3
  Station 4: +5, tank=8, need 2 to reach 0, tank=6
  Station 0: +1, tank=7, need 3 to reach 1, tank=4
  Station 1: +2, tank=6, need 4 to reach 2, tank=2
  Station 2: +3, tank=5, need 5 to reach 3, tank=0
  Complete!

Answer: 3
```

### Alternative: Brute Force

```python
def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    n = len(gas)

    for start in range(n):
        tank = 0
        valid = True

        for i in range(n):
            curr = (start + i) % n
            tank += gas[curr] - cost[curr]
            if tank < 0:
                valid = False
                break

        if valid:
            return start

    return -1
```

Time: O(n^2) - for each start, simulate the circuit.

### Mathematical Insight

The problem can be viewed as finding a "rotation" of the net gains array that has all prefix sums non-negative.

```python
def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    n = len(gas)
    net = [gas[i] - cost[i] for i in range(n)]

    if sum(net) < 0:
        return -1

    # Find starting point where prefix sums are always >= 0
    min_sum = float('inf')
    min_idx = 0
    curr_sum = 0

    for i in range(n):
        curr_sum += net[i]
        if curr_sum < min_sum:
            min_sum = curr_sum
            min_idx = i

    return (min_idx + 1) % n
```

### Edge Cases
- Single station: return 0 if gas[0] >= cost[0]
- All stations have same gas and cost: return 0
- No solution: return -1

### Related Problems
- Minimum Cost to Hire K Workers: greedy selection
- Task Scheduler: circular scheduling
- Circular Array Loop: detect cycles
