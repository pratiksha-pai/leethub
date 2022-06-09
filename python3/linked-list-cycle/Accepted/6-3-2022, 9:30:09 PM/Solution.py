// https://leetcode.com/problems/linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        
        slow_pointer = head
        fast_pointer = head.next
        
        while(slow_pointer!=None and fast_pointer!=None):
            if slow_pointer == fast_pointer:
                return True
            else:
                slow_pointer = slow_pointer.next
                fast_pointer = fast_pointer.next
                if(fast_pointer!=None):
                    fast_pointer=fast_pointer.next
                else:
                    return False
                
        
        return False
        