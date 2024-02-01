# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def get_min(root):
            while root.left:
                root = root.left
            return root.val
        
        def dfs(root, key):
            if root == None:
                return None
            
            if root.val < key:
                root.right = dfs(root.right, key)
            elif root.val > key:
                root.left = dfs(root.left, key)
            else: # key found
                
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                else:
                    
                    root.val = get_min(root.right)
                    root.right = dfs(root.right, root.val)
            
            return root
        
        return dfs(root, key) 