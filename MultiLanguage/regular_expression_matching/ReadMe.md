# [Regular Expression Matching](https://leetcode.com/problems/regular-expression-matching/)

Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".


## Solution Explanation

The tricky part is that '*' can match *zero* or more of the preceding string. So we have to handle that case. The reason this is hard is that it becomes a dynamic programming problem. It is not simple enough to DFS to see if any subsequent patterns match. That would end up very inefficient. Instead we need memoization to efficiently move along. 

To memoize, we need to understand what discrete options are available to us. Given s as the string and pattern p and pointers i iterating over s and j iterating over p: 

s = aac pattern a * a * c 

Since the first a is followed by a star pattern, it can be followed by zero or more a's. Meaning we now need to decide whether to use the next a as part of the original a's. This is a binary decision. Either move the i pointer forward one (continue to search for the same pre-start pattern) or move the j pointer forward 2 (skip the * and evaluate the next).
 
Note this only works because the * trailing can be '0' or more. The memoization method is below (in a Top-down / DFS scenario) 

```
    if (j+1) < len(p) and p[j+1] == "*":
        return ( 
            dfs(i, j+2) # move forward
            or 
            match and dfs(i+1,j) # continue to search the string if the existing string matches the existing pattern
        )
```

It can be implemented in a top-down pattern. 
