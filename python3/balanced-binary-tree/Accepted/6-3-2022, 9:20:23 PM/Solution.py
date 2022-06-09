// https://leetcode.com/problems/balanced-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        h_left = 0
        h_right = 0
        h = 0
        
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        
        if root.left != None:
            h_left = self.height(root.left)
        if root.right != None:
            h_right = self.height(root.right)
        
        if h_left > h_right:
            h = 1 + h_left
        else:
            h = 1 + h_right
        
        return h
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        elif root.left == None and root.right == None:
            return True
        else:
            pass
        
        h_left = self.height(root.left)
        h_right = self.height(root.right)
        if abs(h_left-h_right)>1:
            return False
        
        if root.left != None and self.isBalanced(root.left) == False:
            return False
        
        if root.right != None and self.isBalanced(root.right) == False:
            return False
        
        
        
        return True
        