# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # after learning the algorithm
        self.res=0
        self.covered={None}
        # if the node does not have parents and node is not covered by its children add the node to covered
        # for the leaf, right and left are None and None is already in covered
        # n-node, p-parent
        def dfs(n, p):
            if n==None:
                return 
            
            dfs(n.left, n)
            dfs(n.right, n)
            
            # priority - if children are not covered, cover the, hence coverring your parent
            # if you dont have a parent, you would not be covered by above condition, hence cover yourself, hence covering your children 
            if n.left not in self.covered or n.right not in self.covered or n not in self.covered and p is None:
                self.covered.update({n,n.left,n.right,p})
                self.res+=1
            
        
        dfs(root, None)
        print(self.res)
        return self.res
            