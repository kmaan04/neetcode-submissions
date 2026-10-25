# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow , fast = head, head # start both pointers at the head

        while fast and fast.next: # while fast and fast.next are truthy vals we increment both pointers if check returns false then that means end of linked list reached and no cycle 

            slow = slow.next # move  by 1  links 
            fast = fast.next.next # move by 2 links

            if slow  == fast: #  eventually if cycle exists both pointers will meet at the same node ( only  1 diff b/w them )
                return True
        
        # return False if no cycle  
        return False

        