# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return
        
        curr = head
        arr = []

        while curr:
            arr.append(curr)
            curr = curr.next
        
        front, back = 0, len(arr)-1

        while front < back:
            arr[front].next = arr[back]
            front += 1

            arr[back].next = arr[front]
            back -= 1
        
        arr[front].next = None

        