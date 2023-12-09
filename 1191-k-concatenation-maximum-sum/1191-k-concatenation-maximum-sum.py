class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        MOD = 10**9 + 7
        max_sum1 = 0
        max_sum2 = 0
        curr_sum = 0
        
        
        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum < 0:
                curr_sum = 0
            max_sum1 = max(max_sum1, curr_sum) 
            
        if k == 1:
            return max_sum1
        
        print(max_sum1)
        
        curr_sum = 0
        for it in range(2):
            for i in range(len(arr)):
                curr_sum += arr[i]
                if curr_sum < 0:
                    curr_sum = 0
                max_sum2 = max(max_sum2, curr_sum) 
        
        # print(max_sum1, sum(arr), max_sum2)
        
        return max(max_sum1, max_sum2, (max_sum2 + sum(arr) * (k-2))) % MOD