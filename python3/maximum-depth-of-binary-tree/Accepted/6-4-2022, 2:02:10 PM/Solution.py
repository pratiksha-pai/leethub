// https://leetcode.com/problems/maximum-depth-of-binary-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        
        s1 = []
        s2 = []
        
        h = 0
        s1.append(root)
        
        while(len(s1) != 0 or len(s2) != 0):
            if len(s1)!=0:
                h += 1
            while len(s1) != 0 :
                temp = s1[0]
                
                if temp.left != None:
                    s2.append(temp.left)
                if temp.right != None:
                    s2.append(temp.right)
                
                del s1[0]
            
            if len(s2)!=0:
                h += 1

            while len(s2) != 0 :
                temp = s2[0]
                
                if temp.left != None:
                    s1.append(temp.left)
                if temp.right != None:
                    s1.append(temp.right)
                
                del s2[0]
            
            
        return h
                


            