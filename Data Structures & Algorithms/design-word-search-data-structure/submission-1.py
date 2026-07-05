class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLastChar = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isLastChar = True

    def search(self, word: str) -> bool:

        def searchHelper(self, word:str, i:int, cur) -> bool:
            
            if i >= len(word): # iterated to the end
                if cur.isLastChar:
                    return True
                return False
            
            if word[i] == '.':
                res = False
                for k, v in cur.children.items():
                    if not res:
                        res = searchHelper(self, word, i + 1, v)
                return res
                                    
            if word[i] in cur.children:
                return searchHelper(self, word, i + 1, cur.children[word[i]])
            
            return False
        
        return searchHelper(self, word, 0, self.root)
        
        
