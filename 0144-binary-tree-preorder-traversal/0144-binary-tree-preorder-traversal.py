# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root == None:
            return []
        
        res = []
        curr, s = root, []
        
        while s or curr:
            
            while curr:
                res.append(curr.val)
                s.append(curr)
                curr = curr.left
            
            curr = s.pop()
            curr = curr.right
            
            
            
            
            
        return res
            