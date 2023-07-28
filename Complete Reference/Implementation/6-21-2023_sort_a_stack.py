from os import *
from sys import *
from collections import *
from math import *


def sortStack(stack):
    # given data structure is a python list
    # as list have all the similar operations available so use them
    # Write your code here
    recurse(stack)
    return stack


def recurse(stack):
    if len(stack) == 0:
        return
    ele = stack.pop()
    recurse(stack)
    recurseSort(stack, ele)


def recurseSort(stack, ele):
    if len(stack) == 0:
        stack.append(ele)
        return
    if stack[-1] <= ele:
        stack.append(ele)
        return
    ele1 = stack.pop()
    recurseSort(stack, ele)
    stack.append(ele1)


stackEles = [5, -2, 9, -7, 3]
print(sortStack(stackEles))
