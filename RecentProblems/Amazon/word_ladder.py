"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a 
sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words 
in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.


Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.


It looks like a shortest path problem. 

We could use backtracking 

TIME LIMIT EXCEEDED
dfs
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 

        else:
            shortest = len(wordList)+2

        def backtrack(word, rem_list, cur_len):

            @lru_cache
            def check_one_away(word1, word2):
                for i in range(len(word1)):
                    if word1[i] != word2[i]:
                        return word1[i+1:] == word2[i+1:]

                return True

            nonlocal shortest
            if word == endWord:
                shortest = min(shortest, cur_len)
                return 
            if cur_len >=shortest:
                return 

            for i, word2 in enumerate(rem_list):
                # check if word is one digit away
                if check_one_away(word,word2):
                    backtrack(word2, rem_list[:i]+rem_list[i+1:], cur_len+1)
                
        backtrack(beginWord, wordList, 1)
        return shortest if shortest < len(wordList) + 2 else 0


"""

Modified my DFS with the word dict optimization
"""
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 

        else:
            shortest = len(wordList)+2

        def backtrack(word, cur_len):
            nonlocal shortest
            nonlocal all_combo_dict
            if word == endWord:
                shortest = min(shortest, cur_len)
                return 
            if cur_len >=shortest:
                return 

            for j in range(L):
                semi_word = word[:j]+"*"+word[j+1:]
                for word2 in all_combo_dict[semi_word]:
                    if word2 not in visited:
                        visited.add(word2)
                        backtrack(word2,  cur_len+1)

                    all_combo_dict[semi_word] = []

        L = len(beginWord)
        all_combo_dict = defaultdict(list)
        visited = set()
        for word in wordList:
            for i in range(L):
                all_combo_dict[word[:i]+"*"+word[i+1:]].append(word)

        backtrack(beginWord,  1)
        return shortest if shortest < len(wordList) + 2 else 0

"""
BFS
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0 

        else:
            shortest = len(wordList)+2

        L = len(beginWord)

        q = collections.deque([(beginWord,1)])
        visited = set()
        while q:
            cur_word, level = q.popleft()
            for i in range(L):
                intermediate_word = cur_word[:i] +"*"+cur_word[i+1:]
                for word in all_combo_dict[intermediate_word]:
                    if word == endWord:
                        return level +1
                    if word not in visited:
                        visited.add(word)
                        q.append((word, level+1))

                all_combo_dict[word]=[]

        return 0








