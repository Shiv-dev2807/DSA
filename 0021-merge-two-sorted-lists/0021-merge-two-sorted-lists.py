# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = None
        cur0 = dummy

        cur = list1
        cur1 = list2
        
        while cur and cur1:
            if cur.val < cur1.val:
                cur0.next = cur
                cur = cur.next
            else:
                cur0.next = cur1
                cur1 = cur1.next
            cur0 = cur0.next
        
        cur0.next = cur if cur else cur1

        return dummy.next