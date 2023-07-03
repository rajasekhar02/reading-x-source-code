from typing import List


class Solution:
    """
    Below method works only for array of length n+1 but contains the numbers between within range [1,n]
    eg: n+1 = 5
        n = 4
        so array contains numbers in range [1,4]
    Other Methods:
    Hashing - But uses n amount of space
    Sorting - O((n+1)log(n+1))
    """

    def findDuplicate(self, nums: List[int]) -> int:
        # using cycle method
        oneStep = nums[0]
        twoSteps = nums[0]

        while True:
            oneStep = nums[oneStep]
            twoSteps = nums[nums[twoSteps]]
            if oneStep == twoSteps:
                break

        twoSteps = nums[0]

        while oneStep != twoSteps:
            oneStep = nums[oneStep]
            twoSteps = nums[twoSteps]

        return oneStep
