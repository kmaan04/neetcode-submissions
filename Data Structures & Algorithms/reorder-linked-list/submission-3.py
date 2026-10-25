# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow , fast = head, head.next # beginning pos of pts such that we can find beginning of list 2nd half

        while fast and fast.next: # returns false when fast = None (end of list) and slow.next = elem at end of first half
            slow = slow.next
            fast = fast.next.next

        second = slow.next # gets first elem of 2nd half of list 
        prev = slow.next = None # sets both prev and slow.next to None which isolates both first and 2nd halfs  

        # reverse 2nd half of the list:
        while second:
            tmp = second.next # store val of next node so not lost when ptr reversed
            second.next = prev # flip curr node ptr to prev node
            prev = second # set prev node to curr node
            second = tmp # set curr node to next node
        
        # merge both lists:

        first, second = head, prev # pointers keeping track of head and head  of reversed list / end of list 
        while second: # as sescond will always be shorter
            tmp1, tmp2 = first.next, second.next # store vals of next nodes for both lists so not lose  when merge
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2



        