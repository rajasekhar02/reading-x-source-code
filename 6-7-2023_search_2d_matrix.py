from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        rowLow = 0
        rowHigh = rows
        rowMid = 0
        columnStart = 0
        columnEnd = cols - 1

        while rowLow < rowHigh:
            rowMid = rowLow + ((rowHigh - rowLow) >> 1)
            if matrix[rowMid][columnEnd] < target:
                rowLow = rowMid + 1
            elif matrix[rowMid][columnStart] > target:
                rowHigh = rowMid
            #  Bug 1: This Bugs leads to infinite loop because of element doesnot exist
            #          🔽
            elif (
                matrix[rowMid][columnStart] == target
                or matrix[rowMid][columnEnd] == target
            ):
                return True

        colLow = 0

        colHigh = rows - 1
        colMid = 0
        while colLow < colHigh:
            colMid = colLow + ((colHigh - colLow) >> 1)
            if matrix[rowMid][colMid] < target:
                colLow = colMid + 1
            elif matrix[rowMid][colMid] > target:
                colHigh = colMid
            else:
                print(matrix[rowMid][colMid])
                return True
        return False
