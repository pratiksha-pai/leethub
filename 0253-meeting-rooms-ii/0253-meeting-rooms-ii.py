class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x:x[0])
        res = []
        heapq.heappush(res, intervals[0][1])
        
        for interval in intervals[1:]:
            if interval[0] >= res[0]:
                heapq.heappop(res)
            
            heapq.heappush(res, interval[1])
        
        return len(res)