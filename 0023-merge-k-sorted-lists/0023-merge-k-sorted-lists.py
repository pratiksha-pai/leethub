# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush, heappop
        dummy = ListNode(0)
        curr = dummy
        heap = []
        
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))
        
        while heap:
            val, i, node = heappop(heap)
            
            curr.next = ListNode(val)
            curr = curr.next
            node = node.next
            
            if node:
                heappush(heap, (node.val, i, node))
        
        return dummy.next