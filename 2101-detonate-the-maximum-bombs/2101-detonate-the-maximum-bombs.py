class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        from collections import defaultdict
        n = len(bombs)
        adj = defaultdict(list)
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                dist = (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2
                
                if dist <= (bombs[i][2]) ** 2:
                    adj[i].append(j)
                
        
        # print(adj)
        
        def dfs(parent, visited):
            
            if parent in visited:
                return 0
            visited.add(parent)
            temp = 0
            for child in adj[parent]:
                if child not in visited:
                    temp += dfs(child, visited)
                    
            return temp + 1
                    
        ans = 1
        for parent in list(adj.keys()):
            visited = set()
            ans = max(ans, dfs(parent, visited))
            
        return ans 
        
        