class UnionFind:
    def __init__(self, n):
        
        self.parent = [i for i in range(n)] # parent of every node is itself
        self.rank = [1 for _ in range(n+1)] # initially all nodes are of rank 1 - meaning graph with one node
    
    def find(self, node):
        # iterate through parents to do path compression
        # basically parent update

        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    def union(self, parent1, parent2):
        
        # rank update
        if parent1 != parent2:
            if self.rank[parent1] >= self.rank[parent2]: # parent1's graph is bigger
                self.parent[parent2] = parent1
                self.rank[parent1] += 1
            else:
                self.parent[parent1] = parent2
                self.rank[parent2] += 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import Counter
        uf = UnionFind(n)

        
        for u, v in edges:
            parent1 = uf.find(u)
            parent2 = uf.find(v)
            
            if parent1 != parent2:
                uf.union(parent1, parent2)
                
        for i in range(n):
            uf.find(i)
        
        # print(uf.parent)
        
        counter = Counter(uf.parent)
        return len(counter)
                