from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        # binary search over rows
        # to find the suitable row
        rowLow = 0
        rowHigh = rows - 1
        rowMid = 0
        column = 0
        while rowLow < rowHigh:
            rowMid = rowLow + ((rowHigh - rowLow) >> 1)
            #   Bug 1: should not treat equal and less than elements as same won't work when there is only row
            #   Bug 2: I am not checking with first and last elements of a row
            #                         🔽
            if matrix[rowMid][column] <= target:
                rowLow = rowMid + 1
            elif matrix[rowMid][column] > target:
                rowHigh = rowMid

        colLow = 0
        #     Bug 3: should use cols instead of rows
        #          🔽
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
