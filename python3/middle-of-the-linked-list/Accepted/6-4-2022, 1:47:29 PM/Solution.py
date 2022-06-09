// https://leetcode.com/problems/middle-of-the-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return None
        if head.next == None:
            return head
        
        
        slow_pointer = head
        fast_pointer = head.next 
        
        while(fast_pointer != None):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next 
            if fast_pointer == None:
                return slow_pointer
            fast_pointer = fast_pointer.next 
            if fast_pointer == None:
                return slow_pointer
            pass
        
        return slow_pointer
            