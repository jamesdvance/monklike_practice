# Letter Combinations of a Phone Number

## Summary

Given a string containing digits from 2-9, return all possible letter combinations that the number could represent (like on a phone keypad).

### Key Points
- Each digit maps to 3-4 letters
- Generate all combinations of letters
- Use backtracking or iterative approach

### Optimal Approach
Backtracking through each digit's possible letters.

```python
def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []

    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = []

    def backtrack(index, current):
        if index == len(digits):
            result.append(''.join(current))
            return

        for letter in phone_map[digits[index]]:
            current.append(letter)
            backtrack(index + 1, current)
            current.pop()

    backtrack(0, [])
    return result
```

### Complexity
- Time: O(4^n * n) where n is number of digits
- Space: O(n) for recursion depth

---

## Detailed Explanation

### Problem Analysis

This is a Cartesian product problem. For each digit, we have 3-4 choices. We generate all possible combinations by choosing one letter from each digit's options.

### Phone Keypad Mapping

```
1: (none)   2: abc   3: def
4: ghi      5: jkl   6: mno
7: pqrs     8: tuv   9: wxyz
```

### Decision Tree

For digits = "23":

```
            ""
     /      |       \
    a       b        c
   /|\     /|\      /|\
  ad ae af bd be bf cd ce cf
```

Result: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

### Iterative Approach

Build combinations iteratively:

```python
def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []

    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = ['']

    for digit in digits:
        new_result = []
        for combo in result:
            for letter in phone_map[digit]:
                new_result.append(combo + letter)
        result = new_result

    return result
```

### Using itertools.product

```python
from itertools import product

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []

    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    letter_groups = [phone_map[d] for d in digits]
    return [''.join(combo) for combo in product(*letter_groups)]
```

### BFS Approach

```python
from collections import deque

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []

    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    queue = deque([''])

    for digit in digits:
        size = len(queue)
        for _ in range(size):
            current = queue.popleft()
            for letter in phone_map[digit]:
                queue.append(current + letter)

    return list(queue)
```

### Edge Cases
- Empty string: return []
- Single digit: return list of its letters
- Contains '1' or '0': typically not valid (no letters)

### Why 4^n?

Most digits map to 3 letters, but 7 and 9 map to 4. In the worst case (all 7s or 9s), we have 4^n combinations.

### Related Problems
- Generate Parentheses: similar combinatorial generation
- Combinations: choosing k from n
- Subsets: all possible selections
