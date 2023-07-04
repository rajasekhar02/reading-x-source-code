from collections import defaultdict
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for i in nums:
            # ~ => represents the two's complement of the number
            # ~x == -x-1
            ones ^= i & ~twos
            twos ^= i & ~ones
        return ones

    def singleNumber32N(self, nums: List[int]) -> int:
        ans = 0
        for j in range(0,32):
            sum = 0
            sum1 = 0
            for i in nums:
                # i & (1<<(j)) => 8
                # (i>>j) & 1 => 4
                # sum1 += i & (1<<(j))
                num = i
                if num < 0:
                    num = num & ((1<<32)-1)
                sum += num>>j & 1
            sum = sum % 3
            ans |= sum << j
        if ans >= (1<<31):
            ans -= (1<<32)
        return ans

    def singleNumberVarMem(self, nums: List[int]) -> int:
        uniquesNums = set(nums)
        sumOfUniqueNums = 3*sum(set(nums)) # 3*x1 + 3*x2 + 3*x3 + 3*unique_num
        sumOfNums = sum(nums) # 3*x1 + 3*x2 + 3*x3 + unique_num
        # 3*x1 + 3*x2 + 3*x3 + 3*unique_num - 3*x1 + 3*x2 + 3*x3 + unique_num = 2*unique_nums
        diff = sumOfUniqueNums - sumOfNums  
        print(diff)
        return diff // 2

    def singleNumberVarMem(self, nums: List[int]) -> int:
        dictNums = defaultdict(int)
        for i in nums:
            dictNums[i] += 1
        for i in dictNums:
            if dictNums[i] == 1:
                return i
        return -1