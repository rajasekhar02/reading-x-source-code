# def getInversions(arr, n):
#     # Write your code here.
#     return


def dcModifiedMergeSort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        arr1 = dcModifiedMergeSort(arr, start, mid)
        arr2 = dcModifiedMergeSort(arr, mid + 1, end)

        start1 = 0
        start2 = 0
        newArr = []
        while start1 < len(arr1) and start2 < len(arr2):
            if arr1[start1] > arr2[start2]:
                newArr.append(arr2[start2])
                start2 += 1
                continue
            if arr1[start1] < arr2[start2]:
                newArr.append(arr1[start1])
                start1 += 1
                continue
            newArr.append(arr1[start1])
            newArr.append(arr2[start2])
            start1 += 1
            start2 += 1
        while start1 < len(arr1):
            newArr.append(arr1[start1])
            start1 += 1
        while start2 < len(arr2):
            newArr.append(arr2[start2])
            start2 += 1
        return newArr

    return [arr[start]]


x = [2, 2, 2, 3, 2]
print(dcModifiedMergeSort(x, 0, 4))
