# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pr = None
        cr = head
        
        while cr:
            nex = cr.next
            cr.next = pr
            pr = cr
            cr = nex
        return pr