
from typing import Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
    def __str__(self) -> str:
        return str(self.x)

""" Technique Learned
Main take away is adding new copies to the original list and then seperating them
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # create copy of the node and add that copy to the next
        if head == None: return None
        tempHead = head
        while tempHead != None: 
            temp = tempHead.next
            newNode = Node(tempHead.val, temp, None)
            tempHead.next = newNode
            tempHead = temp
        # add the random pointers to the newNode by traversing over the original list
        tempHead = head 
        while tempHead != None and tempHead.next != None:
            tempHead.next.random = None
            if tempHead.random != None:
                tempHead.next.random = tempHead.random.next
            tempHead = tempHead.next.next
        # self.printList(head)
        newListHead = head.next
        tempNewHead = newListHead
        oldListHead = head
        while tempNewHead != None and tempNewHead.next != None:
            oldListHead.next = tempNewHead.next
            oldListHead = oldListHead.next
            tempNewHead.next = oldListHead.next
            tempNewHead = tempNewHead.next
        return newListHead
    def printList(self, head):
        tempHead = head
        arr = []
        while tempHead != None:
            arr.append(str(tempHead.val))
            tempHead = tempHead.next
        print("->".join(arr))