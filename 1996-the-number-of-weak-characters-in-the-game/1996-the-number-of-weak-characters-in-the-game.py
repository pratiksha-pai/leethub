class Solution:
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        
        p = sorted(p, key = lambda x: (-x[0], x[1]))
        count = 0 
        # print(p)
        max_defense = -1
        for _, defense in p:
            if defense < max_defense:
                count+= 1
            else:
                max_defense = defense

        
        return count