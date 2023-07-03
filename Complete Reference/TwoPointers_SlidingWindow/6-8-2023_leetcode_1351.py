from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        j = cols - 1
        negCount = 0
        # struggled to get this logic
        # Didn't solved the question on paper first
        # Easy problem I took 40 mins to solve
        # if I have solved it on the paper then it could be solved in 15 mins
        for i in range(0, rows):
            while (j >= 0) and (grid[i][j] < 0):
                j -= 1
            negCount += cols - j - 1

        return negCount
