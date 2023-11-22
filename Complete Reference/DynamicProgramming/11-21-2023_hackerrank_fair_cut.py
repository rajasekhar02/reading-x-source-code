def compute_score(group_1, group_2):
    score = 0
    for i in group_1:
        for j in group_2:
            score += abs(i - j)    
    return score

def fairCutGreedy(k, arr):
    arr.sort()
    # if k > n/2
    if 2 * k > n:
        k = n - k
    
    mid = n // 2
    start = (mid - k) 
    stop = mid + k
    group_1, group_2 = [], []

    for i in range(len(arr)):
        # this condition satisfies after i > n/2
        if stop >= i >= start and (i - start) % 2 == 1:
            group_1.append(arr[i])
        else:
            group_2.append(arr[i])
    
    return compute_score(group_1, group_2)

# need to add dp solution