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
        
        
        q = deque([(0, root)])
        res = []
        
        while q:
            # depth, node = q.popleft()
            n = len(q)
            temp = []
            for _ in range(n):
                depth, node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append((depth+1, node.left))
                if node.right:
                    q.append((depth+1, node.right))
                
            # if len(res) == depth:
            #     res.append([])
            # res[depth].append(node.val)
            res.append(temp)

            
        return res
        
        