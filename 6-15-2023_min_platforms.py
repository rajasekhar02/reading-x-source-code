from collections import deque


# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#
class Solution:
    # Function to find the minimum number of platforms required at the
    # railway station such that no train waits.
    def minimumPlatform1(self, n, arr, dep):
        # code here
        flatTrainSchedule = []
        for id, i in enumerate(arr):
            flatTrainSchedule.append([i, id + 1])
            flatTrainSchedule.append([dep[id], id + 1])
        queue = deque()
        flatTrainSchedule = sorted(flatTrainSchedule, key=lambda x: (x[0], x[1]))
        # for i in flatTrainSchedule:
        #     if len(queue) == 0:
        #         queue.append()

    def minimumPlatform(self, n, arr, dep):
        # below two lines are the important in this problem
        arr.sort()
        dep.sort()

        trainSchedule = [[i, dep[id]] for id, i in enumerate(arr)]
        maxPlatforms = 1
        platformCount = 1
        iTrain = 0
        jTrain = 1
        while iTrain < n and jTrain < n:
            jTrainStartTime = trainSchedule[jTrain][0]
            iTrainEndTime = trainSchedule[iTrain][1]
            if iTrainEndTime < jTrainStartTime:
                platformCount -= 1
                iTrain += 1
            elif iTrainEndTime >= jTrainStartTime:
                platformCount += 1
                jTrain += 1
            maxPlatforms = max(
                maxPlatforms, platformCount
            )  # this lines saves the from getting -ve values
        return maxPlatforms

    # def minimumPlatform(self, n, arr, dep):
    #     arr.sort()
    #     dep.sort()

    #     ans = 1
    #     count = 1
    #     i = 1
    #     j = 0
    #     while i < len(arr) and j < len(dep):
    #         if arr[i] <= dep[j]:  # one more platform needed
    #             count += 1
    #             i += 1
    #         else:  # one platform can be reduced
    #             count -= 1
    #             j += 1
    #         ans = max(ans, count)  # updating the value with the current maximum
    #     return ans
    def minimumPlatformNotWorking(self, n, arr, dep):
        trainSchedule = [[i, dep[id]] for id, i in enumerate(arr)]
        trainSchedule = sorted(trainSchedule, key=lambda x: (x[0], -x[1]))
        maxLen = 1
        stack = [trainSchedule[0]]
        for id in range(1, n):
            i = trainSchedule[id]
            if stack[-1][1] >= i[0]:
                stack.append(i)
            else:
                while len(stack) > 0 and stack[-1][1] < i[0]:
                    stack.pop()
                stack.append(i)
            maxLen = max(maxLen, len(stack))
        return maxLen
