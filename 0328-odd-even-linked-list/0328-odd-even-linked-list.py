# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None or head.next == None:
            return head
        
        odd = None
        even = None
        even_head = None
        odd_head = None
        
        t = head
        flag = False
        while t!= None:
            if flag:
                if even == None:
                    even = t
                    even_head = t
                else:
                    even.next = t
                    even = t
            else:
                if odd == None:
                    odd = t
                    odd_head = t
                else:
                    odd.next = t
                    odd = t
            
            t = t.next
            flag = not flag
        
        odd.next = even_head
        even.next = None

#         if odd.next == None:
#         else:
#             even.next = odd_head
#             odd.next = None
    
        return head
            
        