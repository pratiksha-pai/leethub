# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root==None:
            return None
        if root.left==None and root.right==None:
            return root
        
        root.right=self.increasingBST(root.right)
        if root.left==None:
            return root
        
        root.left=self.increasingBST(root.left)
        
        temp=head=root.left
        while temp!=None and temp.right!=None:
            temp=temp.right
        temp.right=root
        root.left=None

        return head