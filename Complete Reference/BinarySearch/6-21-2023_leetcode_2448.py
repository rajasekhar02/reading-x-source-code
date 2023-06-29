from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        # binary search
        # equalNums: 1  2  3  4  5
        #      cost: 10>12=12<10<10
        #             ^  ^  ^
        #            c1 c2 c3
        # Above is the reason for applying binary search
        findCost = lambda equalEle: sum(
            [cost[id] * abs(equalEle - i) for id, i in enumerate(nums)]
        )
        low = min(nums)
        high = max(nums)
        ans = high + 1
        while low <= high:
            mid = (low + high) // 2
            cost1 = findCost(mid - 1)
            cost2 = findCost(mid)
            cost3 = findCost(mid + 1)
            # print(cost1, cost2, cost3)
            if cost1 > cost2 and cost2 > cost3:
                low = mid + 1
            elif cost1 >= cost2 and cost2 <= cost3:
                ans = cost2
                break
            else:
                high = mid - 1
        # print(ans)
        return ans

    def minCostNotWorking(self, nums: List[int], cost: List[int]) -> int:
        minCost = 0
        # diff = 0
        # for i in range(1, len(nums)):
        #     diff += abs(nums[i]-nums[i-1])
        # if diff == 0: return 0
        numsWithCost = sorted([[i, cost[id]] for id, i in enumerate(nums)])
        weightedAvg = round(sum(map(lambda x: x[0] * x[1], numsWithCost)) / sum(cost))

        for i in range(0, len(nums)):
            minCost += abs(weightedAvg - nums[i]) * cost[i]
        tempMinCost = minCost
        minCost = 0
        for i in range(0, len(nums)):
            minCost += abs((weightedAvg) - nums[i]) * cost[i]
        return minCost


# nums = [
#     735103,
#     366367,
#     132236,
#     133334,
#     808160,
#     113001,
#     49051,
#     735598,
#     686615,
#     665317,
#     999793,
#     426087,
#     587000,
#     649989,
#     509946,
#     743518,
# ]
# cost = [
#     724182,
#     447415,
#     723725,
#     902336,
#     600863,
#     287644,
#     13836,
#     665183,
#     448859,
#     917248,
#     397790,
#     898215,
#     790754,
#     320604,
#     468575,
#     825614,
# ]
nums = [1, 3, 5, 2]
cost = [2, 2, 12, 12]
print(Solution().minCost(nums, cost))
