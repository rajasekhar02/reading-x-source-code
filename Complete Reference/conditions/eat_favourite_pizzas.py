from os import *
from sys import *
from collections import *
from math import *

def canIEat(pType, day, maxPPerDay, pTypeCount, prePTypeCount):
    minPs = day + 1
    # Total pizzas should be greater the minimum should be eatten per day
    if (prePTypeCount+pTypeCount) < minPs:
        return 0
    # Days required to complete previous Pizza types by eating at maximum capacity
    daysForPrePTypeCountToComplete = prePTypeCount / maxPPerDay
    if daysForPrePTypeCountToComplete >= (day+1):
        return 0   
    # so from above i can complete prePTypeCount in days
    # pTypeCount = eating the currType pizza 1 per each day
    # day = eating all the previous pizzas before current type before the current days based on the above condition
    # So days required to complete current Pizza type = days +
    daysToCompleteCurrentPType = day+pTypeCount
    if daysToCompleteCurrentPType < (day+1):
        return 0
    return 1

def canCompleteChallenges(arr, mat):
    # Write your code here
    # Return a list of 0's and 1's
    pizzasEaten = [0]
    for i in range(0,len(arr)):
        pizzasEaten.append(pizzasEaten[-1]+arr[i])
    ans = []
    for i in mat:
        [pType, day, maxPPerDay] = i
        prePTypeCount = pizzasEaten[pType]
        ans.append(canIEat(pType, day, maxPPerDay, arr[pType], prePTypeCount))
    return ans
        


