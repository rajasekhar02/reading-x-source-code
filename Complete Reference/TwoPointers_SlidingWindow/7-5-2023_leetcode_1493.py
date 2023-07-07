from collections import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        longestLen = 0
        cntZeros = 0
        for right in range(0, len(nums)):
            cntZeros += nums[right] == 0
            if cntZeros > 1:
                cntZeros -= nums[left] == 0
                left += 1
            longestLen = max(longestLen, right - left)
        return longestLen

    def longestSubarrayVarMem(self, nums: List[int]) -> int:
        compArr = [nums[0]]
        freq = [1]
        for i in range(1, len(nums)):
            if nums[i] != compArr[-1]:
                compArr.append(nums[i])
                freq.append(1)
                continue
            freq[-1] += 1

        if len(compArr) == 1:
            # when len of compArr == 1
            # it can be 0 or 1
            if compArr[0] == 1:
                return freq[0] - 1
            return 0

        start = 0
        if compArr[start] == 0:
            start = 1
        ans = 0
        # covers testcase: 011110011
        # output: 4
        for id, i in enumerate(freq):
            if compArr[id] == 1:
                ans = max(ans, i)
        # covers deletion of one
        for i in range(start, len(compArr) - 2, 2):
            if compArr[i + 1] == 0 and freq[i + 1] == 1:
                ans = max(ans, freq[i] + freq[i + 2])
        return ans
