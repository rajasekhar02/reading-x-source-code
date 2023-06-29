from collections import deque
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) == 0:
            return 0
        maxSequence = 0
        countSequence = 1
        for i in range(1, len(nums)):
            if (nums[i] - nums[i - 1]) == 1:
                countSequence += 1
            elif (nums[i] - nums[i - 1]) == 0:
                countSequence = countSequence
            else:
                if countSequence > maxSequence:
                    maxSequence = countSequence
                countSequence = 1
        if countSequence > maxSequence:
            maxSequence = countSequence
        return maxSequence

    """Learning
    Usage of visited in the BFS to identify the sequence
    """

    def longestConsecutiveBFS(self, nums: List[int]) -> int:
        visited = {}
        for i in nums:
            visited[i] = False
        max_sequence = 0
        for i in nums:
            if visited[i]:
                continue
            queue = deque()
            queue.append(i)
            sequence = 0
            while len(queue) > 0:
                item = queue.popleft()
                sequence += 1
                visited[item] = True
                if ((item + 1) in visited) and visited[item + 1] == False:
                    queue.append(item + 1)
                if ((item - 1) in visited) and visited[item - 1] == False:
                    queue.append(item - 1)

            max_sequence = max(sequence, max_sequence)
        return max_sequence
