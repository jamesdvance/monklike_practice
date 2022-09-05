"""
ALIEN DICTIONARY
There is a new alien language that uses the English alphabet. However, the order among the letters is unknown to you.

You are given a list of strings words from the alien language's dictionary, 
where the strings in words are sorted lexicographically by the rules of this new language.

Return a string of the unique letters in the new alien language sorted in lexicographically 
increasing order by the new language's rules. If there is no solution, return "". If there are multiple solutions, return any of them.

A string s is lexicographically smaller than a string t if at the first letter where they differ, 
the letter in s comes before the letter in t in the alien language. If the first min(s.length, t.length) letters are the same, then s is smaller if and only if s.length < t.length.
"""
from collections import defaultdict, Counter, deque
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # Build adjacency list and indegree
        adj_list = defaultdict(set)
        indegree = Counter({c:0 for word in words for c in word}) # It's a counter, but all zeros

        for first_word, second_word in zip(words, words[1:]):
            same = True
            for c, d in zip(first_word, second_word):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        indegree[d] += 1 

                    same = False
                    break # stop at first non-matching letter

            if same and len(second_word) < len(first_word):
                # invalid
                return ""

        # Khan's 
        output = [] 
        q = deque([c for c in indegree if indegree[c] == 0])

        #visited = set([c for c in indegree if indegree[c] == 0])
        while q:
            c = q.popleft()
            output.append(c)
            # Decrement all children
            for chi in adj_list[c]:
                indegree[chi] -=1 
                if indegree[chi] ==0:
                    #and c not in visited:
                    q.append(chi)

        # Check for a cycle, meaning ordering is invalid
        if len(output) < len(indegree):
            return ""


        return "".join(output)






