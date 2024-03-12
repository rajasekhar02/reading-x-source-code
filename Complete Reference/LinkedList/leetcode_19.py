# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        firstPtr = head
        secondPtr = head
        nthCtItr = n

        while secondPtr != None and nthCtItr > 0:
            secondPtr = secondPtr.next
            nthCtItr -= 1

        while secondPtr and secondPtr.next != None:
            firstPtr = firstPtr.next
            secondPtr = secondPtr.next
        # secondPtr will become only if it is iterated completely in the first while loop
        if secondPtr == None:
            head = firstPtr.next
        else:
            firstPtr.next = firstPtr.next.next
        return head
