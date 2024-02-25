# cheapest flight within k stops
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        MAX = 100000
        cost =  [100000]*n
        cost[src] = 0
        # for flight in flights:
        #     [tSrc, tDest,] 
        for neighbourDistance in range(0, k+1):
            tempCost = cost.copy()
            for flight in flights:
                [tSrc, tDest, tickCost] = flight
                if cost[tSrc] == MAX:
                    continue
                if tempCost[tDest] > (cost[tSrc] + tickCost):
                    tempCost[tDest] = cost[tSrc] + tickCost
            cost = tempCost
        # print(cost)
        if cost[dst] == MAX:
            return -1
        return cost[dst]
