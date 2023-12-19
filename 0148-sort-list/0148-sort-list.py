# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # bad method
        temp = head
        res = []
        while temp != None:
            res.append(temp.val)
            temp = temp.next
        
        res.sort()
        temp = head
        idx = 0
        while temp != None:
            temp.val = res[idx]
            idx += 1 
            temp = temp.next
            
        return head