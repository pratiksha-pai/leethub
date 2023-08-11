class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_the_world = False # see how i wrote world instead of word there, funny no? muhahah

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
            node = node.children[w]
        
        node.end_of_the_world = True

    def search(self, word: str) -> bool:
        node = self.root
        
        for w in word:
            if node == None or w not in node.children:
                return False
            node = node.children[w]
        if node.end_of_the_world == False:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for w in prefix:
            if node == None or w not in node.children:
                return False
            node = node.children[w]
        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)