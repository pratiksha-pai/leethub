class UnionFind:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.rank = [1 for i in range(n)]
        
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])

        return self.p[x]

    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        
        if xp == yp:
            return 
        
        if self.rank[xp] >= self.rank[yp]:
            self.p[yp] = xp
            self.rank[xp] += 1
        else:
            self.p[xp] = yp
            self.rank[yp] += 1

class Solution:
    def findCircleNum(self, isc: List[List[int]]) -> int:
        
        n = len(isc)

        dsu = UnionFind(n)
        res = n
        
        for i in range(n):
            for j in range(i,n):
                if isc[i][j]  and dsu.find(i) != dsu.find(j):
                    res -= 1
                    dsu.union(i, j)
                    
        return res
                    
                