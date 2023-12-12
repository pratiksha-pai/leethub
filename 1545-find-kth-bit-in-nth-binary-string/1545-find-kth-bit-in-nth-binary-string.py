class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        anchors = []
        for i in range(1, n+1):
            if 2**i > k:
                break 
            anchors.append(2**i)
        
        flips = 0
        idx = k
        
        # print(anchors)
        
        while idx != 1:
            curr_anchor = anchors.pop()
            
            if idx == curr_anchor:
                val = '1'
                for i in range(flips):
                    if val == '1':
                        val = '0'
                    else:
                        val = '1'
                
                return val
            if idx > curr_anchor:
                idx = (curr_anchor * 2) - idx
                flips += 1
            # print(curr_anchor, idx)
            
        
        val = '0'
        for i in range(flips):
            if val == '0':
                val = '1'
            else:
                val = '0'
        
        
        return val
            