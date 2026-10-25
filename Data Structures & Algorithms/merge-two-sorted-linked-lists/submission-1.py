# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode() # create a dummy node to help merge lists
        tail = dummy # current end of merged list 

        while list1 and list2: # run loop until either list 1 or 2 run out of elems to append
            if list1.val  < list2.val: # check if curr l1 node less than curr l2 node 
                # if check true above:
                tail.next = list1 # add l1 node to merged list
                list1  = list1.next # get next node in l1
            
            else: # means list1.val >= list2.val
                tail.next = list2 # l2 node smaller so append  to list 
                list2 = list2.next # get next node in l2
            
            tail = tail.next # set curr end of merged list to recently added elem
        
        tail.next = list1 or list2 # checks if list1 or list2 is none and appends rest of truthy list to the tail
        return dummy.next # return new  head of merged list as dummy node just placeholder with no val