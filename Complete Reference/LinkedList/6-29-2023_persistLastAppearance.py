from os import *
from sys import *
from collections import *
from math import *


# List Node Class.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lastAppearanceSlowAndHardToImplement(head):
    # Write your code here.
    dictNodes = defaultdict(lambda: [None,None])
    prevNode = None
    tempNode = head
    while tempNode != None:
        storedNode = dictNodes[tempNode.data]
        if storedNode[0] == None and storedNode[1] == None:
            dictNodes[tempNode.data] = [prevNode,tempNode]
            prevNode = tempNode
            tempNode = tempNode.next
            continue
        # head
        if storedNode[0] == None:
            head = storedNode[1].next
            dictNodes[head.data] = [None, dictNodes[head.data][1]]
            dictNodes[tempNode.data] = [prevNode, tempNode]
            prevNode = tempNode
            tempNode = tempNode.next
            continue
        # tail
        # if storedNode[1] == None:
        #     pass
        # middle nodes
        middleNodePrev = dictNodes[storedNode[0].data][0]
        storedNodeNext = dictNodes[storedNode[0].data][1].next
        middleNodePrev.next = storedNodeNext
        dictNodes[storedNodeNext.data] = [middleNodePrev, storedNodeNext]
        dictNodes[tempNode.data] = [prevNode, tempNode]
        prevNode = tempNode
        tempNode = tempNode.next
    return head
    
def lastAppearance(head):
    # Using stack and set makes the implement easy
    tempHead = head
    stack = []
    while tempHead != None:
        stack.append(tempHead)
        tempHead = tempHead.next
    newHead = None
    knownItems = set()
    while len(stack) > 0:
        item = stack.pop()
        if item.data in knownItems:
            continue
        knownItems.add(item.data)
        newNode = Node(item.data)
        if newHead == None:
            newHead = newNode
        else:
            newNode.next = newHead
            newHead = newNode
    return newHead
        
