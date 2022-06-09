// https://leetcode.com/problems/diameter-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def getMax(self, a, b) -> int:
        if a>b:
            return a
        return b
    
    def height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.getMax(self.height(root.left), self.height(root.right)) + 1
    
    def diameterOfBinaryTreeUtil(self, root: Optional[TreeNode], h) -> int:
        
        if root == None:
            return h

        height_max = self.height(root.left) + self.height(root.right)
        height_left = self.diameterOfBinaryTreeUtil(root.left, 0)
        height_right = self.diameterOfBinaryTreeUtil(root.right, 0)
        
        # print('heightssss')
        # print(height_max, height_left, height_right)
        
        height1 = self.getMax(height_left, height_right)
        height2 = self.getMax(height_max, h)
        height_max = self.getMax(height1, height2)
        
        return height_max
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            return 0
        
        return self.diameterOfBinaryTreeUtil(root, 0)
    
    
    
#     def distanceToLeftLeaf(self, root) -> int:
#         h = 0
#         if root == None :
#             return 0
#         if root.left == None:
#             return 0
        
#         while root.left != None:
#             h += 1 
#             root = root.left
#         # print('from distanceToLeftLeaf - '+str(h))    
#         return h
    
#     def distanceToRightLeaf(self, root) -> int:
#         h = 0
#         if root == None :
#             return 0
#         if root.right == None:
#             return 0
        
#         while root.right != None:
#             h += 1 
#             root = root.right
        
#         # print('from distanceToRightLeaf - '+str(h))
#         return h
    
#     def getDiamter(self, root: Optional[TreeNode], d):
#         if root == None:
#             return 0
#         # if root.left == None and root.right == None:
#         #     return d
        
#         return 1 + getDiamter(root.left, d) + getDiamter(root.right, d)
    
    
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
#         if root == None:
#             return 0
#         if root.left == None and root.right == None:
#             return 0
        
#         return getDiamter(root, 0)
        
        
#         # d_left = self.diameterOfBinaryTree(root.left)
#         # d_right = self.diameterOfBinaryTree(root.right)
        
        
#         # print(self.distanceToLeftLeaf(root))
#         # print(self.distanceToRightLeaf(root))
#         # print(self.diameterOfBinaryTree(root.left))
#         # print(self.diameterOfBinaryTree(root.right))
#         # print('-----------------------------')
        
        
#         # d_max = d
#         # if (d_max < d_left):
#         #     d_max = d_left
#         # if (d_max < d_right):
#         #     d_max = d_right
        
#         return d
        
        
        
        
        
        