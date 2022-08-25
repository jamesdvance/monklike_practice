# Using list to store children

class TrieNode:
    def __init__(self):
        self.children = [None]*26 
        #self.children ={}
        self.end = False 

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Get current Trie Node
        curr = self.root 
        # OVer each letter in word
        for c in word: 
            # Distaance between letter and a. i.e.convert char to i
            i = ord(c)-ord("a")
            # Make a char child if one doesn't exist
            if curr.children[i] == None:
                curr.children[i] = TrieNode()

            curr = curr.children[i]
        # Mark end character
        curr.end=True         

    def search(self, word: str) -> bool:
        curr = self.root 
        for c in word:
            i = ord(c)-ord("a")
            if curr.children[i] == None:
                return False 
            curr = curr.children[i]

        return curr.end
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root 
        for c in prefix:
            i = ord(c)-ord("a")
            if curr.children[i] == None:
                return False 
            curr = curr.children[i]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# Using dictionary to store children

class TrieNode:
    def __init__(self):
        self.children ={}
        self.end = False 

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Get current Trie Node
        curr = self.root 
        # OVer each letter in word
        for c in word: 
            # Distaance between letter and a. i.e.convert char to i
            if c in 
            # Make a char child if one doesn't exist
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]
        # Mark end character
        curr.end=True         

    def search(self, word: str) -> bool:
        curr = self.root 
        for c in word:
            if c not in curr.children:
                return False 
            curr = curr.children[c]

        return curr.end
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root 
        for c in prefix:
            if c not in curr.children:
                return False 
            curr = curr.children[c]

        return True