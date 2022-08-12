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

        p_val=p.val
        q_val=q.val
        
        if p_val>q_val:
            temp=p_val
            p_val=q_val
            q_val=temp
        

        while root!=None:
            # print(root)
            if root.val < q_val and root.val < p_val:
                return self.lowestCommonAncestor(root.right, p, q)
            elif root.val > q_val and root.val > p_val:
                return self.lowestCommonAncestor(root.left, p, q)
            else:
                return root
        
        
        return None
            