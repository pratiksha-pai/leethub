class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        from heapq import heappush, heappop 
        intervals = sorted(intervals, key = lambda x: x[0])
        print(intervals)
        
        res = []
        heappush(res, intervals[0][1])
        
        for start, end in intervals[1:]:
            if start >= res[0]:
                heappop(res)
            heappush(res, end)
        
        return len(res)