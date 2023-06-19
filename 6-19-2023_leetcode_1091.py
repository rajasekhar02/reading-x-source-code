from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        gridSize = len(grid)
        if grid[0][0] == 1: return -1
        queue = deque()
        queue.append([[0,0],1])
        minPath = 500
       
        while len(queue) > 0:
            [pos, path] = queue.popleft()
            # print(pos)
            if pos[0] == gridSize-1 and pos[1] == gridSize-1:
                return path
            grid[pos[0]][pos[1]] = -1 
            directions = [
                [-1,-1],[-1,0],[-1,1],
                [0, -1],[0, 0],[0, 1],
                [1, -1],[1, 0],[1, 1]
            ]
            for i in directions:
                if (pos[0] + i[0]) >= gridSize or (pos[0]+i[0]) < 0:
                    continue
                if (pos[1] + i[1]) >= gridSize or (pos[1]+i[1]) < 0:
                    continue
                newPosX = pos[0] + i[0]
                newPosY = pos[1] + i[1]
                # print(newPosX, newPosY)
                if grid[newPosX][newPosY] == 1 or grid[newPosX][newPosY] == -1:
                    continue
                queue.append([[newPosX,newPosY],path+1])
        # if minPath == 500:
        return -1
        # return minPath