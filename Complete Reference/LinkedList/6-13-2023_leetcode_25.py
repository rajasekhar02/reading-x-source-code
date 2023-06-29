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
        newHead = self
        arr = [str(self.val)]
        while newHead.next != None:
            newHead = newHead.next
            arr.append(str(newHead.val))
        return "->".join(arr)

    def __repr__(self):
        newHead = self
        arr = [str(self.val)]
        while newHead.next != None:
            newHead = newHead.next
            arr.append(str(newHead.val))
        return "->".join(arr)


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tempHead = head
        newHead = None
        tempK = k
        prevSubListEnd = None
        while tempHead != None:
            subListHead = tempHead
            subListEnd = None
            while tempK > 0 and tempHead != None:
                subListEnd = tempHead
                tempHead = tempHead.next
                tempK -= 1
            if tempK > 0:
                prevSubListEnd.next = subListHead
                break
            subListEnd.next = None
            tempK = k
            tempNewHead = self.reverseLL(subListHead)
            if prevSubListEnd == None:
                prevSubListEnd = subListHead
            else:
                prevSubListEnd.next = tempNewHead
                prevSubListEnd = subListHead
            if newHead == None:
                newHead = tempNewHead
        return newHead

    def reverseLL(self, head):
        newHead = head
        nextNewHead = newHead.next
        newHead.next = None
        while nextNewHead != None:
            nextNextNewHead = nextNewHead.next
            nextNewHead.next = newHead
            newHead = nextNewHead
            nextNewHead = nextNextNewHead
        return newHead


k = 2
head = [1, 2]
print(Solution().reverseKGroup(ListNode.listToLinkedList(head), k))
