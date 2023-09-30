class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        import heapq
        from collections import defaultdict
        
        int_max = 2**32 -1
        visited = set()
        costs = [int_max for _ in range(n+1)]
        costs[k] = 0
        graph = defaultdict(list)
        pq = [(0, k)]
        
        for u, v, w in times:
            graph[u].append((v, w))
        
        
        while pq:
            
            cost_src, src = heapq.heappop(pq)
            
            for neigh, wei in graph[src]:
                new_cost = cost_src + wei
                if new_cost < costs[neigh]:
                    costs[neigh] = new_cost 
                    heapq.heappush(pq, (new_cost, neigh))
                    
        
        # print(costs)
        res = max(costs[1:])
        return res if res != int_max else -1
                