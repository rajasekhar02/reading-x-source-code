# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newHead = ListNode(0, head) # Trick 1
        nextItr = newHead
        currVal = head.val
        prefixSumDict = defaultdict(lambda: None)
        while nextItr != None:
            currVal += nextItr.val
            if prefixSumDict[currVal] != None:
                preStart = prefixSumDict[currVal]
                start = preStart.next
                prevVal = currVal + start.val
                while prevVal != currVal:
                    del prefixSumDict[prevVal]
                    start = start.next
                    prevVal = prevVal + start.val
                preStart.next = start.next
            else:
                prefixSumDict[currVal] = nextItr
            nextItr = nextItr.next
        return newHead.next
