# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], sv: int, dv: int) -> str:
        
        def get_path(node, val):
            if not node:
                return ''
            
            if node.val == val:
                return 'X'
            
            l = get_path(node.left, val)
            if l:
                return 'L' + l
            
            r = get_path(node.right, val)
            if r:
                return 'R' + r
            
            return ''
    
        def common_ancestor(a, b):
            i = 0
            while i < min(len(a), len(b)) and a[i] == b[i]:
                i+=1
            return 'U' * (len(a) - i) + b[i:]
        
        path1 = get_path(root, sv)[:-1]
        path2 = get_path(root, dv)[:-1]
        
        return common_ancestor(path1, path2)
    
        