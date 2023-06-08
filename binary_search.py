def binary_search(arr, start, end, search_element):
    pass


# all elements will be greater than or equal to the given search_element
# arr[ind] >= search_element
# Smallest index such that arr[ind] >= search_element
# both start and end are inclusive [start, end]
# means end should be length - 1
def lower_bound(arr, start, end, search_element):
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


# all elements after ind will be greater than the given search_element
# arr[ind] > search_element
# smallest index such that arr[ind] > search_element
# both start and end are inclusive [start, end]
# means end should be length - 1
def upper_bound(arr, start, end, search_element):
    low = start
    high = end
    ans = end + 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] > search_element:
            high = mid - 1
            ans = mid
        else:
            low = mid + 1
    return ans
