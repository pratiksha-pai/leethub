class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        from functools import cmp_to_key
        
        n = len(nums)
        # nums = list(reversed(sorted(nums, key=cmp_to_key(lambda x, y:((str(x) + str(y)) < (str(y) + str(x)))))))
        nums = sorted(nums, key=cmp_to_key(lambda x, y: -1 if str(x) + str(y) > str(y) + str(x) else (1 if str(x) + str(y) < str(y) + str(x) else 0)))
        
        return str(int("".join(str(nums[i]) for i in range(len(nums)))))
            