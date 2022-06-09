// https://leetcode.com/problems/climbing-stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        # fibonacci sequece 
        res = []
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        res.append(1)
        res.append(1)
        
        for i in range(2, n+1):
            # print(res[i-1])
            # print(res[i-2])
            # temp = res[i-1]
            
            res.append((res[i-1] + res[i-2]))
        
        return res[n]
            