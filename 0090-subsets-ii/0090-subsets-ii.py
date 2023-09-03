class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        
        res = [[]]
        nums.sort()
        for num in nums:
            temp = []
            for x in res:
                x = x + [num]
                if x not in res:
                    temp.append(x)
            res.extend(temp[:])
        
        # print(res)
        return res