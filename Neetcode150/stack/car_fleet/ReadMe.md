# Car Fleet

## Summary

`n` cars are heading toward a target, each starting at position `position[i]` with speed `speed[i]`. A car cannot pass another car, so when it catches up, they form a fleet traveling at the slower car's speed. Return the number of fleets that arrive at the target.

### Key Points
- Cars closer to target determine if cars behind can catch up
- Process cars from closest to target to farthest
- Cars that catch up merge; cars that do not form new fleets

### Optimal Approach
Sort by position (closest to target first). For each car, calculate time to reach target. If a car behind arrives at the same time or earlier, it joins the fleet; otherwise, it forms a new fleet.

```python
def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)
    fleets = 0
    prev_time = 0

    for pos, spd in cars:
        time = (target - pos) / spd
        if time > prev_time:
            fleets += 1
            prev_time = time

    return fleets
```

### Complexity
- Time: O(n log n) - dominated by sorting
- Space: O(n) - for the sorted list

---

## Detailed Explanation

### Problem Analysis

The key insight is that a slower car ahead blocks faster cars behind it. If a faster car would reach the target before the car ahead, it must slow down and join that fleet. The arrival time of a fleet is determined by the slowest (leading) car.

### Why Process from Closest to Target

By processing cars from closest to target, each car's potential arrival time is compared to the fleet ahead. If it would arrive sooner, it joins that fleet. If it would arrive later, it leads a new fleet.

### Time Calculation

Time to reach target from position `p` at speed `s`:
```
time = (target - p) / s
```

This is the time if the car could travel unimpeded. If this time is less than or equal to the time of the car ahead, the car catches up and joins the fleet.

### Stack-Based Solution

Using an explicit stack:

```python
def carFleet(target: int, position: list[int], speed: list[int]) -> int:
    cars = sorted(zip(position, speed), reverse=True)
    stack = []

    for pos, spd in cars:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)

    return len(stack)
```

The stack holds the arrival times of fleet leaders. We only push when a car does not catch up to the fleet ahead.

### Step-by-Step Example

For `target = 12`, `position = [10, 8, 0, 5, 3]`, `speed = [2, 4, 1, 1, 3]`:

Sort by position (descending):
- (10, 2): time = 2/2 = 1.0
- (8, 4): time = 4/4 = 1.0
- (5, 1): time = 7/1 = 7.0
- (3, 3): time = 9/3 = 3.0
- (0, 1): time = 12/1 = 12.0

Processing:
- (10, 2): time=1.0 > 0, new fleet, prev_time=1.0
- (8, 4): time=1.0 <= 1.0, catches up, same fleet
- (5, 1): time=7.0 > 1.0, new fleet, prev_time=7.0
- (3, 3): time=3.0 <= 7.0, catches up, same fleet
- (0, 1): time=12.0 > 7.0, new fleet, prev_time=12.0

Result: 3 fleets

### Why Not Use <=

We use `time > prev_time` (not `>=`) because if times are exactly equal, the car behind catches up right at the target and joins the fleet.

### Handling Equal Positions

If two cars start at the same position, they are already a fleet. The sorting is stable, so they stay together, and the slower one (longer time) determines the fleet time.

### Edge Cases
- Single car: 1 fleet
- All cars same speed: as many fleets as gaps (some may never catch up)
- Car at target position: instant arrival, time = 0
- All cars already at target: all have time = 0, form 1 fleet

### Related Problems
- Car Fleet II: find time until collision
- Minimum Speed to Arrive on Time: related to travel time calculation
- Meeting Scheduler: similar interval/collision concepts
