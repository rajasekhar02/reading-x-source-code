from typing import List
from collections import deque
from heapq import heapify, heappush, heappop
import math
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        gridSize = len(grid)
        if grid[0][0] == 1: return -1
        pq = []
        dest = [gridSize-1,gridSize-1]
        heappush(pq, (math.dist([0,0],dest),[0,0],1))
        minPath = 500
        while len(pq) > 0:
            # print(pq)
            dirDist, pos, path = heappop(pq)
            print(dirDist,pos)
            if pos[0] == gridSize-1 and pos[1] == gridSize-1:
                return path
            grid[pos[0]][pos[1]] = -1 
            # visited.add(pos)
            directions = [
                [-1,-1],[-1,0],[-1,1],
                [0, -1],[0, 0],[0, 1],
                [1, -1],[1, 0],[1, 1],
            ]
            for i in directions:
                if (pos[0] + i[0]) >= gridSize or (pos[0]+i[0]) < 0:
                    continue
                if (pos[1] + i[1]) >= gridSize or (pos[1]+i[1]) < 0:
                    continue
                newPosX = pos[0] + i[0]
                newPosY = pos[1] + i[1]
                newPos = [newPosX, newPosY]
                # print(newPosX, newPosY)
                if grid[newPosX][newPosY] == 1 or grid[newPosX][newPosY] == -1:
                    continue
                heappush(pq,(math.dist(newPos, dest)+path,[newPosX,newPosY],path+1))
            if pos[0] == 4 and pos[1] == 4:
                print(pq)
        if minPath == 500:
            return -1
        return minPath

grid = [
    [0,0,1,0,0,1,0,1,0],
    [0,0,0,0,0,0,0,0,0],
    [0,1,1,0,1,1,1,1,1],
    [0,0,0,1,0,0,0,0,0],
    [1,1,0,0,0,1,0,0,0],
    [1,0,1,0,0,1,0,0,1],
    [1,1,1,1,0,0,1,0,0],
    [1,0,0,1,0,0,1,1,1],
    [0,0,0,0,0,0,0,0,0]]
# grid = [[0,0,0],[1,1,0],[1,1,0]]
print(Solution().shortestPathBinaryMatrix(grid))