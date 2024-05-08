class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        g = defaultdict(list)
        
        for u, v, w in flights:
             g[u].append((v, w))
        
        heap = [[0, k+1, src]]
        dist = defaultdict(lambda: defaultdict(lambda: float('inf')))
        dist[src][k+1] = 0
        
        while heap:
            cost, stops_left, u = heapq.heappop(heap)
            if u == dst:
                return cost
            
            if stops_left <= 0:
                continue
            
            for v, w in g[u]:
                if cost+w < dist[v][stops_left-1]:
                    heapq.heappush(heap, [cost+w, stops_left-1, v])
                    dist[v][stops_left-1] = cost+w
        
        return -1