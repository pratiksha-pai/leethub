class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        
        node.end = True

    def searchChild(self, word:str, node:TrieNode) -> bool:
        
        if len(word) == 0:
            return node.end
        
        w = word[0]
        if w == '.':
            for k, v in node.children.items():
                if self.searchChild(word[1:], node.children[k]) == True:
                    return True
                
            return False
        elif w not in node.children:
            return False
        else:
            return self.searchChild(word[1:], node.children[w])
        
        return False
        
        
    def search(self, word: str) -> bool:
        node = self.root
        
        return self.searchChild(word, node)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)