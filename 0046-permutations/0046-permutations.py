class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        n = len(nums)
        
        def backtrack(path, used):
            if len(path) == n:
                # print(path)
                res.append(path[:])

            for i in range(len(nums)):
                if i not in used:
                    used.add(i)
                    backtrack(path + [nums[i]], used)
                    used.remove(i)

        
        backtrack([], set())
        return res