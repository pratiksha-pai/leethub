// https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len1 = 0
        len2 = 0
        len_diff = 0
        
        
        tempA = headA
        tempB = headB
        
        while(tempA!=None or tempB!=None):
            if tempA!=None:
                tempA=tempA.next
                len1+=1
            if tempB!=None:
                tempB=tempB.next
                len2+=1
            
        tempA = headA
        tempB = headB
        
        if len1 > len2:
            count = len1 - len2
            while count!=0:
                tempA=tempA.next
                count-=1
            
        else:
            count = len2 - len1
            while count!=0:
                tempB=tempB.next
                count-=1
        
        
        while(tempA!=tempB and tempA!=None and tempB!=None):
            tempA=tempA.next
            tempB=tempB.next
        
        if tempA==tempB:
            return tempA
        
        return None