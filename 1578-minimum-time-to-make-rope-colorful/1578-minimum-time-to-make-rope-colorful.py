class Solution:
    def minCost(self, colors: str, nt: List[int]) -> int:
        
        n= len(colors)
        res = 0
        max_cost = nt[0]
        
        for i in range(1, n):
            if colors[i] == colors[i-1]:
                
                res += min(max_cost, nt[i])
                max_cost = max(max_cost, nt[i])
            else:
                max_cost = nt[i]
        

        return res