from collections import defaultdict


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        hashNums = defaultdict(list)
        for i in range(0, len(nums)):
            hashNums[nums[i]].append(i)
        maxTotalLen = 1
        for i in hashNums:
            gap = 0
            start = 0
            end = start + 1
            indices = hashNums[i]
            while end < len(indices):
                # why -1 ? -> to exclude the extremes from the calculating gap
                # taking the gaps between adjacent elements
                gap += indices[end] - indices[end - 1] - 1
                # print(gap)
                while gap > k and start < len(indices):
                    gap -= indices[start + 1] - indices[start] - 1
                    start += 1
                maxTotalLen = max(maxTotalLen, end - start + 1)
                # print(end, start, i, gap)
                end += 1
        return maxTotalLen
