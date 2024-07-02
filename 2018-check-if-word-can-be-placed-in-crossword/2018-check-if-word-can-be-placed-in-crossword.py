class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        
        R, C = len(board), len(board[0])
        word_reversed = word[::-1]
        
        def check_horizontal(x, y, word):
            if y-1 >= 0 and board[x][y-1] != '#':
                return False
            if y + len(word) < C and board[x][y+len(word)] != '#':
                return False
            for i in range(len(word)):
                if y+i >= C or (board[x][y+i] != ' ' and board[x][y+i] != word[i]):
                    return False
            
            return True
                
        def check_vertical(x, y, word):
            if x-1 >= 0 and board[x-1][y] != '#':
                return False
            if x+len(word) < R and board[x+len(word)][y] != '#':
                return False
            for i in range(len(word)):
                if x+i >= R or (board[x+i][y] != ' ' and board[x+i][y] != word[i]):
                    return False
            
            return True
        
        for x in range(R):
            for y in range(C):
                if (y==0 or board[x][y-1] == '#') and (y+len(word)-1) < C:
                    if check_horizontal(x, y, word) or check_horizontal(x, y, word[::-1]):
                        return True
                if (x==0 or board[x-1][y] == '#') and (x+len(word)-1) < R:
                    if check_vertical(x, y, word) or check_vertical(x, y, word[::-1]):
                        return True
        
        return False
        