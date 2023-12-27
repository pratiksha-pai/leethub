class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        num_fives = 0
        
        while n >0:
            n//=5
            num_fives += n
        
        return num_fives
            