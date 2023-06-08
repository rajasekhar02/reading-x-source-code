from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        inversions = [0]
        self.dcModifiedMergeSort(nums, 0, len(x) - 1, inversions)
        return inversions[0]

    def dcModifiedMergeSort(self, arr, start, end, inversions):
        if start < end:
            mid = (start + end) // 2
            self.dcModifiedMergeSort(arr, start, mid, inversions)
            self.dcModifiedMergeSort(arr, mid + 1, end, inversions)

            temp = []

            # Most of the time is wasted at getting this logic right
            for i in range(mid + 1, end + 1):
                pos = self.lower_bound(arr, start, mid + 1, (2 * arr[i]) + 1)
                if pos > mid:
                    continue
                inversions[0] += mid - pos + 1

            start1 = start
            start2 = mid + 1

            while start1 <= mid and start2 <= end:
                if arr[start1] > arr[start2]:
                    temp.append(arr[start2])
                    start2 += 1
                elif arr[start1] < arr[start2]:
                    temp.append(arr[start1])
                    start1 += 1
                else:
                    temp.append(arr[start1])
                    temp.append(arr[start2])
                    start1 += 1
                    start2 += 1

            while start1 <= mid:
                temp.append(arr[start1])
                start1 += 1

            while start2 <= end:
                temp.append(arr[start2])
                start2 += 1

            for i in range(start, end + 1):
                arr[i] = temp[i - start]

    def lower_bound(self, arr, start, end, search_element):
        low = start
        high = end
        ans = end + 1
        while low <= high:
            mid = low + ((high - low) // 2)
            if arr[mid] >= search_element:
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans


# def just_less_than(arr, start, high, search_element):
#     for i in range(start, high+1)

x = [1, 3, 2, 3, 1]
inversions = [0]
print(Solution().dcModifiedMergeSort(x, 0, len(x) - 1, inversions), inversions, x)
