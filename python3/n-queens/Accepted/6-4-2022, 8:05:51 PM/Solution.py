// https://leetcode.com/problems/n-queens

class Solution:
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        # prohibited cells if we have the queen on (i, j)
        # (i, j)  --> (i+1, j+1) --> (i+2, j+2) --> ...
        # (i, j)  --> (i+1, j-1) --> (i+2, j-2) --> ...
        
        
        # cur - current row
        # path - current placement within this path
        # prev - all prev queen places
        # ans - all configurations list
        
		# check if (cur, col) cell is availible considering all queens above
        def check(col, cur, prev):
            if not prev: return True
            for i, j in prev:
                if col == j: return False
                if cur - i == abs(col - j): return False
            return True
        
        def dfs(cur, prev, path):
            
            if cur == n:
                ans.append(path)
                return
            
            for col in range(n):
                if check(col, cur, prev):
                    new_line = '.'*col + 'Q' + '.'*(n-col-1)
                    dfs(cur + 1, prev + [(cur, col)], path + [new_line])
        
        ans = []
        dfs(0, [], [])
        return ans