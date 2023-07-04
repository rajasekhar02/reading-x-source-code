class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        compressedList = [nums[0]]
        freq = [1]
        for i in range(1,len(nums)):
            if compressedList[-1] != nums[i]:
                compressedList.append(nums[i])
                freq.append(1)
                continue
            freq[-1] += 1
        # print(freq)
        if len(compressedList) == 1:
            return int(compressedList[0] == 1)
        freq[0] = 0
        ans = 1
        constant = 1e9 + 7
        start = 0
        if compressedList[0] == 1:
            start = 1
        for i in range(start, len(compressedList), 2):
            if (i+1) == len(compressedList):
                break
            # print(i, freq[i])
            if compressedList[i+1] == 1:
                ans = ans*(freq[i]+1)
                ans = ans % constant
        return int(ans)