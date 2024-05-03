# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        from collections import defaultdict
        res = defaultdict(list)
        level = []
        res[0].append(root.val)
        level.append((0, root))
        
        while level:
            n = len(level)
            for _ in range(n):
                idx, node = level.pop(0)
                if node.left:
                    res[idx-1].append(node.left.val)
                    level.append((idx-1, node.left))
                if node.right:
                    res[idx+1].append(node.right.val)
                    level.append((idx+1, node.right))
        
        return [ans for _, ans in sorted(res.items())]
                
        