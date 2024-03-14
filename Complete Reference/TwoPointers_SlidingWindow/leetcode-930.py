# check this link for solution explanation: https://www.notion.so/Coding-Round-d3b5440fcd914fab9d6f8f3a0bd7b87f?pvs=4#90c2e48ceb62450f91d4d576d9d3b5c8
class Solution:
    def numSubarraysWithSum2(self, nums: List[int], goal: int) -> int:
        total_count = 0
        curr_sum = 0
        freq = defaultdict(int)
        for num in nums:
            curr_sum += num
            if curr_sum == goal:
                total_count += 1
            if freq[curr_sum - goal] != 0:
                total_count += freq[curr_sum-goal]
            freq[curr_sum] += 1
        return total_count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def slidingWindowAtMost(nums, goal):
            start = 0
            curr_sum = 0
            total_count = 0
            for end in range(0, len(nums)):
                curr_sum += nums[end]
                while (start <= end) and (curr_sum > goal):
                    curr_sum -= nums[start]
                    start += 1
                total_count += (end-start+1)
            return total_count
        return slidingWindowAtMost(nums, goal) - slidingWindowAtMost(nums, goal-1)
