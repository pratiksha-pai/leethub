# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def find_path(node, val):
            if node == None:
                return ''
            
            if node.val == val:
                return 'x'
            
            left = find_path(node.left, val)
            if left:
                return 'l' + left
            
            right = find_path(node.right, val)
            if right:
                return 'r' + right
            
            return ''
        
        def ca(a, b): # comon ancestor
            i = 0
            while i < min(len(a), len(b)) and a[i] == b[i]:
                i+= 1
            return 'u' * (len(a) - i) + b[i:]
        
        path1 = find_path(root, startValue)[:-1]
        path2 = find_path(root, destValue)[:-1]
        
        return ca(path1, path2).upper()