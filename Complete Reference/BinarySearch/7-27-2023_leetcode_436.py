class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        newIntervals = [ [i, id] for id, i in enumerate(intervals)]
        newIntervals = sorted(newIntervals, key= lambda x: x[0][0])
        ans = [0] * len(newIntervals)
        # print(newIntervals)
        for id, i in enumerate(newIntervals):
            index = self.binarySearch(newIntervals, id, len(newIntervals)-1, i[0][1])
            ans[i[1]] = index
            if index > -1:
                ans[i[1]] = newIntervals[index][1]
        return ans

    def binarySearch(self, intervals, start, end, ithIntervalEnd):
        low = start
        high = end
        ans = -1
        while low <= high:
            # with the below formula able to search from given start index
            mid = low + ((high-low) // 2)
            jIntervalStart = intervals[mid][0][0]
            if  jIntervalStart >= ithIntervalEnd:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        # print(ans)
        return ans
