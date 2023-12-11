class Solution:
    def shortestWordDistance(self, wd: List[str], w1: str, w2: str) -> int:
        
        w1_lis = []
        w2_lis = []
        
        for i in range(len(wd)):
            if w1 == wd[i]:
                w1_lis.append(i)
            if w2 == wd[i]:
                w2_lis.append(i)
        
        min_dis = 10**5 + 1
        
        i, j = w1_lis.pop(), w2_lis.pop()
        
        while True:
            if i != j:
                min_dis = min(min_dis, abs(i-j))

            if len(w1_lis) == 0 and len(w2_lis) == 0:
                return min_dis
            elif i >= j and w1_lis:
                i = w1_lis.pop()
            elif j > i and w2_lis:
                j = w2_lis.pop()
            else:
                return min_dis
                        
        return 0
        
            
            