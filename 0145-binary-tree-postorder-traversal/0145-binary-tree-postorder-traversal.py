# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []

        res = []
        curr, s = root, [root]
        
        while s:
            curr = s.pop()

            res.append(curr.val)
            if curr.left:
                s.append(curr.left)
            if curr.right:
                s.append(curr.right)
                        
        
        return res[::-1]
                    
            
            