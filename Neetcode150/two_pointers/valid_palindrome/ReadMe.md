# Valid Palindrome

## Summary

Given a string `s`, return `true` if it is a palindrome after converting all uppercase letters to lowercase and removing all non-alphanumeric characters.

### Key Points
- A palindrome reads the same forward and backward
- Use two pointers from both ends moving toward the center
- Skip non-alphanumeric characters during comparison

### Optimal Approach
Use two pointers starting from the beginning and end. Move inward, skipping non-alphanumeric characters, and compare characters.

```python
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

### Complexity
- Time: O(n) - each character visited at most once
- Space: O(1) - only using two pointer variables

---

## Detailed Explanation

### Problem Analysis

This problem introduces the two-pointer technique for palindrome checking. The key insight is that if a string is a palindrome, the first character must equal the last, the second must equal the second-to-last, and so on. Two pointers let us check this efficiently.

### Why Two Pointers Work

Instead of reversing the string and comparing (O(n) space), we compare characters in-place:
- Left pointer starts at the beginning
- Right pointer starts at the end
- Both move toward the center
- If any comparison fails, it is not a palindrome

### Alternative Approaches

**Cleaned String Comparison**
Create a cleaned version and compare with its reverse:

```python
def isPalindrome(s: str) -> bool:
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
```

- Time: O(n)
- Space: O(n) for the cleaned string

This is more readable but uses extra space.

**Recursive Approach**

```python
def isPalindrome(s: str) -> bool:
    def helper(left, right):
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if left >= right:
            return True
        if s[left].lower() != s[right].lower():
            return False
        return helper(left + 1, right - 1)

    return helper(0, len(s) - 1)
```

Not recommended due to potential stack overflow on long strings.

### Edge Cases
- Empty string: considered a palindrome
- String with only non-alphanumeric characters: becomes empty, so palindrome
- Single character: palindrome
- All same characters: palindrome
- Case differences: "A" and "a" are considered equal

### Common Mistakes
- Forgetting to skip non-alphanumeric characters
- Not handling case insensitivity
- Off-by-one errors with pointer movement
- Not checking `left < right` inside the skip loops

### The Palindrome Pattern

This two-pointer palindrome check is a building block for:
- Valid Palindrome II (can remove one character)
- Palindromic Substrings (count all palindromes)
- Longest Palindromic Substring (find the longest)
- Palindrome Partitioning (split into palindromes)

### Related Problems
- Valid Palindrome II: allowed to remove one character
- Palindrome Linked List: same concept on a linked list
- Longest Palindromic Substring: find longest palindrome within string
