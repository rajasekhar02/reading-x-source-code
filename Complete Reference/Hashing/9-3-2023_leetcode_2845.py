from typing import List
from collections import defaultdict


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        arrFreqCnt = []
        for id, i in enumerate(nums):
            arrFreqCnt.append((i % modulo) == k)
        dictFreq = defaultdict(int)
        ans = 0
        total = 0
        for i in arrFreqCnt:
            total += i
            mod_value = total % modulo
            # general case
            ans += mod_value == k
            # handles: mod 1 + mod 2 == 3 mod
            ans += dictFreq[(mod_value - k + modulo) % modulo]
            dictFreq[mod_value] += 1
        return ans
