"""
Testcases:
5 3 2 1 4 - random order
5 3 2 1 40 - fail the program sorting is performed on strings
13 5 8 19 2 10 17 4 15 6 12 1 9 11 16 7 20 3 14 18 - 20 numbers shuffled randomly
"""

strListOfNumbers = input()


def prettyPrint(sortType, listOfInts, comparisons):
    print(
        sortType.ljust(30, " "), "|", " ".join(map(str, listOfInts)), "|", comparisons
    )


print(
    "Sorting type".ljust(30, " "),
    "|",
    "List".ljust(len(strListOfNumbers), " "),
    "|",
    "Comparisons",
)
# Bubble Sort
"""
    5 3 2 1 4
    ^ ^
    i j
"""

# Bubble Sort pivot start
listOfNumbers = [int(i) for i in strListOfNumbers.split(" ")]
comparisons = 0
for i in range(0, len(listOfNumbers)):
    for j in range(i + 1, len(listOfNumbers)):
        comparisons += 1
        if listOfNumbers[i] > listOfNumbers[j]:
            temp = listOfNumbers[i]
            listOfNumbers[i] = listOfNumbers[j]
            listOfNumbers[j] = temp
prettyPrint("Bubble Sort pivot start", listOfNumbers, comparisons)


# Bubble Sort pivot end
comparisons = 0
listOfNumbers = [int(i) for i in strListOfNumbers.split(" ")]
for i in range(len(listOfNumbers), 0, -1):
    for j in range(0, i - 1):
        comparisons += 1
        if listOfNumbers[i - 1] < listOfNumbers[j]:
            temp = listOfNumbers[i - 1]
            listOfNumbers[i - 1] = listOfNumbers[j]
            listOfNumbers[j] = temp
prettyPrint("Bubble Sort pivot end", listOfNumbers, comparisons)


# Recursive Bubble Sort
comparisons = 0
listOfNumbers = [int(i) for i in strListOfNumbers.split(" ")]


def recursiveBubbleSort(listOfNumbers, i):
    comparisons = 0
    if i < len(listOfNumbers):
        comparisons = recursiveBubbleSort(listOfNumbers, i + 1)
    for j in range(0, i - 1):
        comparisons += 1
        if listOfNumbers[i - 1] < listOfNumbers[j]:
            temp = listOfNumbers[i - 1]
            listOfNumbers[i - 1] = listOfNumbers[j]
            listOfNumbers[j] = temp
    return comparisons


comparisons = recursiveBubbleSort(listOfNumbers, 0)
prettyPrint("Recursive Bubble Sort", listOfNumbers, comparisons)


# Insertion sort
comparisons = 0
listOfNumbers = [int(i) for i in strListOfNumbers.split(" ")]
for i in range(0, len(listOfNumbers) - 1):
    for j in range(i + 1, 0, -1):
        # inner loop is running only using j
        # i is used as a range limiter
        comparisons += 1
        if listOfNumbers[j - 1] < listOfNumbers[j]:
            temp = listOfNumbers[j - 1]
            listOfNumbers[j - 1] = listOfNumbers[j]
            listOfNumbers[j] = temp
        else:
            break
prettyPrint("Insertion Sort", listOfNumbers, comparisons)


# Recursive Insertion Sort
comparisons = 0
listOfNumbers = [int(i) for i in strListOfNumbers.split(" ")]


def recursiveInsertionSort(listOfNumbers, i):
    comparisons = 0
    if i < len(listOfNumbers) - 1:
        comparisons = recursiveInsertionSort(listOfNumbers, i + 1)
    for j in range(i, len(listOfNumbers) - 1):
        # inner loop is running only using j
        # i is used as a range limiter
        comparisons += 1
        if listOfNumbers[j + 1] > listOfNumbers[j]:
            temp = listOfNumbers[j + 1]
            listOfNumbers[j + 1] = listOfNumbers[j]
            listOfNumbers[j] = temp
        else:
            break
    return comparisons


comparisons = recursiveInsertionSort(listOfNumbers, 0)
prettyPrint("Recursive Insertion Sort", listOfNumbers, comparisons)

# Selection Sort


# Merge Sort
def mergeSort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        arr1 = mergeSort(arr, start, mid)
        arr2 = mergeSort(arr, mid + 1, end)

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


# Quick Sort
