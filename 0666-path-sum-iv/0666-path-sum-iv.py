class Solution:
    def pathSum(self, nums: List[int]) -> int:
        
        # tree = {(level, pos): val}
        tree = {(num//100, (num//10) %10): num%10 for num in nums}
        
        
        print(tree)
        
        def dfs(node, running_sum):
            
            if node not in tree:
                return 0
            
            running_sum += tree[node]
            depth, pos = node
            left = (depth + 1, 2*pos -1)
            right = (depth + 1, 2*pos)
            
            if left not in tree and right not in tree:
                return running_sum

            return dfs(left, running_sum) + dfs(right, running_sum)
        
        return dfs((1,1), 0)
            