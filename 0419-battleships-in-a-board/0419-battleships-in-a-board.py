class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        R, C = len(board), len(board[0])
        def dfs(x, y, horizontal=False):
            if x < 0 or y < 0 or x>= R or y >= C or board[x][y] != 'X':
                return
            
            if horizontal:
                dfs(x+1, y, horizontal)
            else:
                dfs(x, y+1, horizontal)
            
            board[x][y] = '0'
        
        res = 0
        for x in range(R):
            for y in range(C):
                if board[x][y] == 'X':
                    dfs(x, y, True) 
                    board[x][y] = 'X'
                    dfs(x, y, False)
                    res += 1
        return res
                    