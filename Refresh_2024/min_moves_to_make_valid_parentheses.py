"""
921. Minimum Add to Make Parentheses Valid
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.


Initial thoughts:

total number of parentheses must be equal

A two pointer could be used to keep track of the number of parentheses that need to be closed 

The imbalance of open to closed parentheses is the number of moves 

Algorithm steps:

1. Open two pointers (could also initialize two queues)
2. on the left, increment when ) and decrement when  (
3. On the right, increment when ( and decrement when )

New plan 

1. Use a FIFO queue
2. If its (  add it to the queue
3. If its ) pop one item out of the queue unless the queue length is 0, then increment the answer
4. Return the length of the queue + existing answer

())))
(()()()()
)()()()(

"""
import queue
class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        ans = 0
        q = queue.deque([])

        for paren in s:
            if paren == "(":
                q.append("(")
            if paren == ")":
                if q:
                    q.popleft()
                else:
                    ans+=1

        
        return len(q) + ans

