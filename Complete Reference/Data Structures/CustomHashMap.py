"""
You've created a new programming language, and now you've decided to add hashmap support to it. Actually you are quite disappointed that in common programming languages it's impossible to add a number to all hashmap keys, or all its values. So you've decided to take matters into your own hands and implement your own hashmap in your new language that has the following operations:

insert x y - insert an object with key x and value y.
get x - return the value of an object with key x.
addToKey x - add x to all keys in map.
addToValue y - add y to all values in map.

To test out your new hashmap, you have a list of queries in the form of two arrays: queryTypes contains the names of the methods to be called (eg: insert, get, etc), and queries contains the arguments for those methods (the x and y values).

Your task is to implement this hashmap, apply the given queries, and to find the sum of all the results for get operations
"""
from collections import defaultdict
def solution(queryType, query):
    dictNums = defaultdict(int)    
    countGets = 0
    keyOffset = 0
    valueOffset = 0
    enteredInsert = False
    for i in range(0, len(queryType)):
        if queryType[i] == "insert":
            if keyOffset == 0:
                dictNums[query[i][0]] = query[i][1]- valueOffset
            else:
                dictNums[query[i][0]-keyOffset] = query[i][1] - valueOffset
            enteredInsert = True
        elif queryType[i] == "addToValue" and enteredInsert:
            valueOffset += query[i][0]
        elif queryType[i] == "addToKey":
            keyOffset += query[i][0]
        elif queryType[i] == "get":
            countGets += dictNums[query[i][0]-keyOffset] + valueOffset
    return countGets
