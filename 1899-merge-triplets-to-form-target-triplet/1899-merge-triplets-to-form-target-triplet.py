class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        ans = [0, 0, 0]
        
        for i in range(len(triplets)):
            
            should_include = True
            for j in range(3):
                if triplets[i][j] > target[j]:
                    should_include = False # do not include 
            
            if should_include == True:
                for j in range(3):
                    ans[j] = max(ans[j], triplets[i][j])

                    
        return ans == target
