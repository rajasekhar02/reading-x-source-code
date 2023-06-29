from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def listToLinkedList(arr):
        prevNode = None
        for i in range(len(arr) - 1, -1, -1):
            temp = ListNode(arr[i], None)
            temp.next = prevNode
            prevNode = temp
        return prevNode

    def __str__(self):
        if self == None:
            return ""
        newHead = self
        arr = [str(self.val)]
        while newHead.next != None:
            newHead = newHead.next
            arr.append(str(newHead.val))
        return "->".join(arr)

    def __repr__(self):
        if self == None:
            return ""
        newHead = self
        arr = [str(self.val)]
        while newHead.next != None:
            newHead = newHead.next
            arr.append(str(newHead.val))
        return "->".join(arr)


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        newHead = ListNode(0, None)
        dummy = newHead
        currHead1 = list1
        currHead2 = list2

        while currHead1 != None and currHead2 != None:
            if currHead1.val >= currHead2.val:
                dummy.next = currHead2
                currHead2 = currHead2.next
                dummy = dummy.next
            elif currHead1.val < currHead2.val:
                dummy.next = currHead1
                currHead1 = currHead1.next
                dummy = dummy.next
            # prevHead = prevHead.next

        if currHead1 != None:
            dummy.next = currHead1
        if currHead2 != None:
            dummy.next = currHead2
        return newHead.next


k = 2
head1 = [-1, 0, 1, 2, 4]
head2 = [5, 6, 7, 8, 9]
print(
    Solution().mergeTwoLists(
        ListNode.listToLinkedList(head1), ListNode.listToLinkedList(head2)
    )
)
