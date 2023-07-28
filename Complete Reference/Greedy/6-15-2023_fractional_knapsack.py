from typing import Optional


class Item:
    def __init__(self, val, w):
        self.value = val
        self.weight = w


class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W: int, arr: "Optional[Item]", n: int) -> int:
        # code here

        # this code is unnecessary
        # dividing by value/weight => cost of 1 unit
        # dividing by value * (min_weight/weight) => cost of item in term of lowest weight

        # min_weight = arr[0].weight
        # for i in range(1, len(arr)):
        #     if min_weight > arr[i].weight:
        #         min_weight = arr[i].weight

        arr = sorted(arr, key=lambda x: -(x.value * (1 / x.weight)))

        curr_bag_weight = 0
        iItem = 0
        profit = 0
        while iItem < len(arr) and curr_bag_weight < W:
            if (curr_bag_weight + arr[iItem].weight) > W:
                profit += arr[iItem].value * ((W - curr_bag_weight) / arr[iItem].weight)
                curr_bag_weight += W - curr_bag_weight
            else:
                profit += arr[iItem].value
                curr_bag_weight += arr[iItem].weight
            iItem += 1
        return profit
