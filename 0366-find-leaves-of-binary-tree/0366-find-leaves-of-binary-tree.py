# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        def dfs(node):
            if not node:
                return -1
            
            l = dfs(node.left)
            r = dfs(node.right)
            curr = max(l, r) + 1
            if len(res) == curr:
                res.append([])
            res[curr].append(node.val)
            return curr
        
        dfs(root)
        return res