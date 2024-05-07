class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[0])
        res = []
        heapq.heappush(res, intervals[0][1])
        
        for s, e in intervals[1:]:
            if s >= res[0]:
                heapq.heappop(res)
            heapq.heappush(res, e)
        
        return len(res)
            