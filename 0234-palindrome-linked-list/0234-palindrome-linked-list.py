# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        slow = cur
        fast = cur
        
        while fast and fast.next:
            
            slow = slow.next
            fast = fast.next.next
        
        
        cur2 = slow
        p = None
        while cur2:
            nex = cur2.next
            cur2.next = p
            p = cur2
            cur2 = nex
        
        left = head
        right = p
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True