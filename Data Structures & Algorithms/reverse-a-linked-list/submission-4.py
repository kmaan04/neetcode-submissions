# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None # will be new head of the list once reversed, also tracks curr nodes prev node
        curr = head # start at beginning of ll
        
        while curr: # while curr list node is not none
            tmp = curr.next # holds curr nodes next node so list is not lost when reversing the link
            curr.next = prev # reverse link at curr node to its prev
            prev = curr # set prev node to curr 
            curr = tmp # set curr node to next node 
        
        return prev