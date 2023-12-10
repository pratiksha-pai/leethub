# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        def dfs(root, max_num):
            nonlocal res
            if root == None:
                return 
            # print(root.val, max_num)
            
            if root.val >= max_num:
                max_num = root.val
                res += 1
            
            dfs(root.left, max_num)
            dfs(root.right, max_num)
        
        dfs(root, -10**4-1)
        
        return res