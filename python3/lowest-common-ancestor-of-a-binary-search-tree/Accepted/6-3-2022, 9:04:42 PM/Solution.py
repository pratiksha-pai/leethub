// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None:
            return None
        
        if p.val<q.val:
            temp1=p.val
            temp2=q.val
        else:
            temp1=q.val
            temp2=p.val
        
        
        
        if root.val < temp2 and root.val > temp1 or root.val == p.val or root.val == q.val:
            return root
        elif root.val < q.val and root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        return None
        
        