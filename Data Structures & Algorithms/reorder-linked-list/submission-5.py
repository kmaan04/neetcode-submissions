# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow , fast =  head, head.next

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next

        right = slow.next 
        prev = slow.next = None

        while right:
            tmp = right.next
            right.next = prev
            prev = right
            right = tmp
        
        left,  right = head, prev

        while right:
            tmp1, tmp2 = left.next, right.next
            left.next = right 
            right.next = tmp1
            left = tmp1  
            right = tmp2
        
        