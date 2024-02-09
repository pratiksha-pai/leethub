# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        
        def dfs(node):
            if node == None:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)
            h = max(left, right) + 1
            if h == len(res):
                res.append([])
            res[h].append(node.val)
            return h
        
        res = []
        dfs(root)
        return res