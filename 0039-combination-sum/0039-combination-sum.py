class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        if len(candidates) == 0:
            return []
        
        def bt(curr_sum, total_sum, curr_list, final_list): # as the name sugggests its not backtrack, its bad trip
            
            if curr_sum == total_sum:
                final_list.append(curr_list[:])
                return
            if curr_sum > total_sum:
                return
            # i have reached the final and i have nowhere to go, how do i find you in code
            
                
            
            for i in range(len(candidates)):
                
                if not curr_list or candidates[i] >= curr_list[-1]:
                    new_list = curr_list[:]
                    new_list.append(candidates[i])
                    bt(curr_sum + candidates[i], total_sum, new_list, final_list)

            return
        
        bt(0, target, [], res)
        
        return res
                