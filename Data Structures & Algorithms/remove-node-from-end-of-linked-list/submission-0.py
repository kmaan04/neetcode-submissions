# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def reverse(node):
            curr, prev = node, None
            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            return prev

        rev_head = reverse(head)

        node_to_remove = None
        curr, prev1 = rev_head, None

        while curr:
            if n > 1:
                prev1 = curr
                curr = curr.next
                n -= 1
            else:
                node_to_remove = curr
                break

        next_node = node_to_remove.next
        if prev1:
            prev1.next = next_node
        else:
            rev_head = next_node   # if node to remove is head
        node_to_remove.next = None

        return reverse(rev_head)
            

