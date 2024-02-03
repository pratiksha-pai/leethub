class Trie:
    def __init__(self):
        self.children = {}
        self.eow = False
    
    def add_word(self, word):
        node = self
        
        for w in word:
            if w not in node.children:
                node.children[w] = Trie()
            node = node.children[w]
                
        node.eow = True

            
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        root = Trie() 
        for word in words:
            root.add_word(word)
        
        
        R, C = len(board), len(board[0])
        res, visit = set(), set()
        
        dirs = [[-1,0], [1, 0], [0, -1], [0, 1]]

        def dfs(x, y, node, path):
            if x < 0 or y < 0 or x >= R or y >= C or (x, y) in visit or board[x][y] not in node.children:
                return
            
            visit.add((x, y))
            node = node.children[board[x][y]]
            path += board[x][y]
            # print(path)
            if node.eow:
                res.add(path)
                # node.eow = False
            
            for dx, dy in dirs:
                dfs(x+dx, y+dy, node, path)
            
            visit.remove((x, y))
            
        
        for x in range(R):
            for y in range(C):
                dfs(x, y, root, "")
        
        return list(res)
            
            
            
        
        
        
            
            
            
        