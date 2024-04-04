class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a: heapq.heappush(heap, (-a, 'a'))
        if b: heapq.heappush(heap, (-b, 'b'))
        if c: heapq.heappush(heap, (-c, 'c'))
        
        res = ""
        
        while heap:
            count, char = heapq.heappop(heap)
            
            if len(res) >= 2 and res[-1] == res[-2] == char:
                if not heap:
                    break
                new_count, new_char = heapq.heappop(heap)
                new_count += 1
                res += new_char
                if new_count: heapq.heappush(heap, (new_count, new_char))
            else:
                res += char
                count += 1
            if count: heapq.heappush(heap, (count, char))
        
        return res
                