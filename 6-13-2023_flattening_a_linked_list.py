#  https://practice.geeksforgeeks.org/problems/flattening-a-linked-list/1
def flatten(root):
    # Your code here
    tempRoot1 = root
    tempRoot2 = tempRoot1.next
    while tempRoot1 != None and tempRoot2 != None:
        tempRoot2Next = tempRoot2.next
        tempRoot1 = merge(tempRoot1, tempRoot2)
        tempRoot2 = tempRoot2Next
    return tempRoot1


def merge(list1, list2):
    newHead = Node(0)
    dummy = newHead
    currHead1 = list1
    currHead2 = list2
    while currHead1 != None and currHead2 != None:
        if currHead1.data >= currHead2.data:
            dummy.bottom = currHead2
            currHead2 = currHead2.bottom
            dummy = dummy.bottom
        elif currHead1.data < currHead2.data:
            dummy.bottom = currHead1
            currHead1 = currHead1.bottom
            dummy = dummy.bottom
    if currHead1 != None:
        dummy.bottom = currHead1
    if currHead2 != None:
        dummy.bottom = currHead2
    return newHead.bottom
