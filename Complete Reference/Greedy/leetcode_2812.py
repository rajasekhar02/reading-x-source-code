class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        MAX_VALUE = float(inf)
        d_t = [[MAX_VALUE]*cols for i in range(rows)]
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        def bfsOfCellsMinMahattanDistToThief(init_state):
            queue = deque(init_state)
            max_dist = 0
            while len(queue):
                i,j = queue.popleft()
                for e_dir in dirs:
                    newX = i + e_dir[0]
                    newY = j + e_dir[1]
                    if (0 <= newX < rows) and \
                        (0 <= newY < cols) and \
                        (grid[newX][newY] == 0) and \
                        (newX, newY) not in visited:
                        dist = abs(newX-i) + abs(newY-j) + d_t[i][j]
                        if dist > d_t[newX][newY]:
                            continue
                        max_dist = max(max_dist, dist)
                        d_t[newX][newY] = dist
                        visited.add((newX, newY))
                        queue.append((newX, newY))
            return max_dist

        def doesPathExistWith(maxSafeFactor):
            stack = deque()
            stack.append((0,0))
            if d_t[0][0] < maxSafeFactor:
                return False
            while len(stack) > 0:
                posX, posY = stack.pop()
                if (posX == rows-1)  and (posY == cols-1):
                    return True
                for e_dir in dirs:
                    newX = posX + e_dir[0]
                    newY = posY + e_dir[1]
                    if (0 <= newX < rows) and \
                        (0 <= newY < cols) and \
                        (newX, newY) not in visited:
                        if d_t[newX][newY] < maxSafeFactor:
                            continue
                        visited.add((newX, newY))
                        stack.append((newX, newY))
            return False
        
        # collect thief coors
        thief_coor = []
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    thief_coor.append((i,j))
                    d_t[i][j] = 0
        # set dist for cells to thief cells
        visited = set()
        max_dist = bfsOfCellsMinMahattanDistToThief(thief_coor)   
        # print(d_t)    
        # binary search
        def binary_search():
            low = 0
            high = max_dist
            ans = 0
            while low <= high:
                mid = low + (high - low) // 2
                visited = set()
                max_safe_factor_exists = doesPathExistWith(mid)
                # print(mid, max_safe_factor_exists)
                if max_safe_factor_exists:
                    low = mid + 1
                    ans = max(ans, mid)
                else:
                    high = mid - 1
            return ans
        # best first search
        visited = set()
        def BestFirstSearch():
            pq = []
            heapq.heappush(pq, (-d_t[0][0], 0, 0))
            while len(pq) > 0:
                dist, posX, posY = heapq.heappop(pq)
                if (posX == rows-1)  and (posY == cols-1):
                    return -dist
                for e_dir in dirs:
                    newX = posX + e_dir[0]
                    newY = posY + e_dir[1]
                    if (0 <= newX < rows) and \
                        (0 <= newY < cols) and \
                        (newX, newY) not in visited:
                        visited.add((newX, newY))
                        # Important Step         ||||||||||
                        heapq.heappush(pq, (-min(-dist, d_t[newX][newY]), newX, newY))
            return 0

        return BestFirstSearch()
