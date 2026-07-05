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

        def searchHelper(j, cur):
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if searchHelper(i + 1, child):
                            return True
                    return False
                
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            
            return cur.isLastChar
        
        return searchHelper(0, self.root)
                
    