# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        res = defaultdict(list)
        q = deque([(root, 0)])
        
        while q:
            node, dist = q.popleft()
            res[dist].append(node.val)
            if node.left:
                q.append([node.left, dist-1])
            if node.right:
                q.append([node.right, dist+1])
                
            


        return [items for _, items in sorted(res.items())]
            