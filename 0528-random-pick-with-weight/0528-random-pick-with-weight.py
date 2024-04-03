class Solution:

    def __init__(self, weis: List[int]):
        self.presum = []
        presum = 0
        for wei in weis:
            presum += wei
            self.presum.append(presum)
        
        self.total = presum


    def pickIndex(self) -> int:
        target = self.total * random.random()
        l, h = 0, len(self.presum)
        while l < h:
            m = l + ( h - l ) // 2
            if target > self.presum[m]:
                l = m+1
            else:
                h = m
        return l
                
                





# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()