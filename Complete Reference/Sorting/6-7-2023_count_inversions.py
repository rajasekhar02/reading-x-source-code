def dcModifiedMergeSort(arr, start, end, inversions):
    if start < end:
        mid = (start + end) // 2
        arr1 = dcModifiedMergeSort(arr, start, mid, inversions)
        arr2 = dcModifiedMergeSort(arr, mid + 1, end, inversions)

        start1 = 0
        start2 = 0
        newArr = []

        while start1 < len(arr1) and start2 < len(arr2):
            if arr1[start1] > arr2[start2]:
                newArr.append(arr2[start2])
                start2 += 1
                # got struck with this logic and I was able to figure it out
                inversions[0] += len(arr1) - start1
                continue
            if arr1[start1] < arr2[start2]:
                newArr.append(arr1[start1])
                start1 += 1
                continue
            newArr.append(arr1[start1])
            newArr.append(arr2[start2])
            start1 += 1
            start2 += 1

        # This is unnecessary as the counting is already done in the above while loop
        # if start1 == 0:
        #     inversions[0] += len(arr2) * (len(arr1) - 1)

        while start1 < len(arr1):
            newArr.append(arr1[start1])
            start1 += 1

        while start2 < len(arr2):
            newArr.append(arr2[start2])
            start2 += 1
        return newArr

    return [arr[start]]


x = [5, 6, 3, 4]
inversions = [0]
print(dcModifiedMergeSort(x, 0, len(x) - 1, inversions), inversions)
