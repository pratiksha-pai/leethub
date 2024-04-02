# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root] + inorder(root.right)
        
        nodes = inorder(root)
        sorted_nodes = sorted(nodes, key = lambda x:x.val)
        
        swapped  = [node for node, swapped_node in zip(nodes, sorted_nodes) if node.val != swapped_node.val]
        
        swapped[0].val, swapped[1].val = swapped[1].val, swapped[0].val
        