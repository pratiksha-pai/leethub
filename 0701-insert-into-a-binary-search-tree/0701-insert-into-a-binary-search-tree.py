# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        
        # give the appropriate leaf to insert on
        def dfs(root):
            if root == None:
                return None
            
            # print(root.val)
            
            if root.left == None or root.right == None:
                if root.right == None and root.val < val:
                    root.right = TreeNode(val)
                elif root.left == None and root.val > val:
                    root.left = TreeNode(val)
            
            if root.val > val:
                dfs(root.left)
            else:
                dfs(root.right)
            
        dfs(root)   
        
        return root