# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], t: int) -> List[Optional[TreeNode]]:
        
        
        
        def dfs(node):
            if node == None:
                return [None, None]
            elif node.val <= t:
                left, right = dfs(node.right)
                node.right = left
                return [node, right]
            else:
                left, right = dfs(node.left)
                node.left = right 
                return [left, node]

        return dfs(root)