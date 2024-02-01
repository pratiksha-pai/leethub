# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        from collections import deque
        if root == None:
            return []
        
        
        res = []

        def bfs(root):
            
            if root == None:
                return []
            
            temp= []
            p = deque([root])
            q = deque()
            
            while p or q:
                while p:
                    top = p.popleft()
                    temp.append(top.val)
                    if top.left:
                        q.append(top.left)
                    if top.right:
                        q.append(top.right)
                
                p = q
                q = deque()
                res.append(temp)
                temp = []
           
        bfs(root)
        return res