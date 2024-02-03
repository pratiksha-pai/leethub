class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        def backtrack(path):
            if len(path) == n:
                # print(path)
                res.append(path[::])

            for i in range(len(nums)):
                x = nums.pop(i)
                backtrack(path + [x])
                nums.insert(i, x)
        
        
        backtrack([])
        return res