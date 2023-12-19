# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def merge(x, y):
            if not x or not y:
                return x or y
            
            if x.val < y.val:
                x.next = merge(x.next, y)
                return x
            else:
                y.next = merge(x, y.next)
                return y
    
        def sort(node):
            if node == None or node.next == None:
                return node
            
            slow, fast = node, node.next 
            
            while fast and fast.next:
                fast = fast.next.next 
                slow = slow.next 
            
            mid = slow.next 
            slow.next = None
            
            left = sort(node)
            right = sort(mid)
    
            return merge(left, right)
        
        head = sort(head)
        return head
            
            