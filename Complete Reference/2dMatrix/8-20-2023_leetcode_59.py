class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = []
        for i in range(0, n):
            matrix.append([])
            for j in range(0, n):
                matrix[i].append(0)

        rims = n >> 1
        nums = 0
        for i in range(rims):
            rows = i
            cols = i
            while cols < (n - i - 1):
                matrix[rows][cols] = nums + 1
                nums += 1
                cols += 1

            while rows < (n - i - 1):
                matrix[rows][cols] = nums + 1
                nums += 1
                rows += 1

            while cols > i:
                matrix[rows][cols] = nums + 1
                nums += 1
                cols -= 1

            while rows > i:
                matrix[rows][cols] = nums + 1
                nums += 1
                rows -= 1
        if n & 1:
            matrix[rims][rims] = nums + 1
        return matrix
