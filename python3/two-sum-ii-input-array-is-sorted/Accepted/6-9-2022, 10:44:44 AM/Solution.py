// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[]
        low=0
        high=len(numbers)-1
        while low<=high:
            if numbers[low]+numbers[high]==target:
                res.append(low+1)
                res.append(high+1)
                return res
            elif numbers[low]+numbers[high]<target:
                low=low+1
            else:
                high=high-1
            
        return res
