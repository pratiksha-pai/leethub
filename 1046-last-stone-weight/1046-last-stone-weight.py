class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        import heapq
        mheap = []
        
        for i in range(len(stones)):
            heapq.heappush(mheap, -stones[i])
        
        print(mheap)
        
        while len(mheap) > 1:

            x = -heapq.heappop(mheap)
            y = -heapq.heappop(mheap)
            if x == y:
                continue
            else:
                x = abs(x-y)
            
            heapq.heappush(mheap, -x)
        
        return -mheap[0] if len(mheap) else 0
            