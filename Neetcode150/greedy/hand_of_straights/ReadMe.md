# Hand of Straights

## Summary

Given an array of integers representing cards, determine if they can be rearranged into groups of consecutive cards, each group having exactly groupSize cards.

### Key Points
- Sort and greedily form groups starting from smallest
- Use a counter/map to track remaining cards
- Each card must be start of or extend a consecutive sequence

### Optimal Approach
Sort and greedily form groups.

```python
from collections import Counter

def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False

    count = Counter(hand)

    for card in sorted(count.keys()):
        if count[card] > 0:
            num_groups = count[card]
            for i in range(groupSize):
                if count[card + i] < num_groups:
                    return False
                count[card + i] -= num_groups

    return True
```

### Complexity
- Time: O(n log n) for sorting
- Space: O(n) for the counter

---

## Detailed Explanation

### Problem Analysis

Each card must belong to exactly one group. Starting from the smallest card, we must form a group. Then we process the next smallest remaining card, and so on.

### Why Start from Smallest?

The smallest card can only be the start of a group (nothing smaller to extend). So we're forced to form a group starting with it.

### Step-by-Step Example

```
hand = [1, 2, 3, 6, 2, 3, 4, 7, 8], groupSize = 3

count = {1:1, 2:2, 3:2, 4:1, 6:1, 7:1, 8:1}

Card 1: 1 group starting at 1
  Need: 1, 2, 3
  count = {1:0, 2:1, 3:1, 4:1, 6:1, 7:1, 8:1}

Card 2: 1 group starting at 2
  Need: 2, 3, 4
  count = {1:0, 2:0, 3:0, 4:0, 6:1, 7:1, 8:1}

Card 6: 1 group starting at 6
  Need: 6, 7, 8
  count = {1:0, 2:0, 3:0, 4:0, 6:0, 7:0, 8:0}

All cards used. Answer: True
```

### Alternative with Heap

```python
import heapq
from collections import Counter

def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False

    count = Counter(hand)
    min_heap = list(count.keys())
    heapq.heapify(min_heap)

    while min_heap:
        start = min_heap[0]

        for i in range(groupSize):
            card = start + i
            if count[card] == 0:
                return False
            count[card] -= 1
            if count[card] == 0:
                if card != min_heap[0]:
                    return False  # Gap in sequence
                heapq.heappop(min_heap)

    return True
```

### Alternative: Track Open Groups

```python
from collections import Counter

def isNStraightHand(hand: list[int], groupSize: int) -> bool:
    if len(hand) % groupSize != 0:
        return False

    count = Counter(hand)
    open_groups = Counter()  # Groups waiting for next card

    for card in sorted(hand):
        if count[card] == 0:
            continue

        if open_groups[card] > 0:
            # Extend an existing group
            open_groups[card] -= 1
            if card + groupSize - 1 > card:  # Group not complete
                open_groups[card + 1] += 1
        else:
            # Start a new group
            for i in range(groupSize):
                if count[card + i] == 0:
                    return False
                count[card + i] -= 1
            # After forming group of groupSize, no open group

        count[card] -= 1

    return True
```

### Edge Cases
- Length not divisible by groupSize: return False
- groupSize = 1: always True
- All same cards: False unless groupSize = 1
- Already sorted consecutive: straightforward grouping

### Related Problems
- Divide Array in Sets of K Consecutive Numbers: identical problem
- Split Array into Consecutive Subsequences: variable length
- Minimum Adjacent Swaps to Arrange: rearrangement with swaps
