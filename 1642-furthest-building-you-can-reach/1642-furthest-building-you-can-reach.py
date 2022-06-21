class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        #GREEDY APPROACH
        LaddersUsed = []
        for ind in range(len(heights)-1):
            diff = heights[ind+1]-heights[ind]
            if diff <= 0: continue
                
            # Just assuming that I used ladder to jump to next building
            heappush(LaddersUsed,diff)
            
            # if I used all ladders 
            # then I have to check at which jump I need to use bricks instead of ladders
            if len(LaddersUsed) > ladders:
                bricks -= heappop(LaddersUsed)
                
                # This means I dont have sufficient bricks so I cant jump further
                if bricks < 0:
                    
                    # returning current building index
                    return ind
        
        # when I reached last building successfully
        return len(heights)-1
