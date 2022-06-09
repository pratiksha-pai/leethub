// https://leetcode.com/problems/invert-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root

        if root.left == None and root.right == None:
            return root

        if root.right != None:
            root.right = self.invertTree(root.right)
        if root.left != None:
            root.left = self.invertTree(root.left)
        
        temp = root.left 
        root.left = root.right
        root.right = temp
        
        return root 
