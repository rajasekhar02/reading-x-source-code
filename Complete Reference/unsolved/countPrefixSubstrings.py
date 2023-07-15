from collections import Counter


def groupsOfK(strList, k):
    counter = Counter()
    for s in strList:
        for j in range(len(s)):
            prefix = s[: j + 1]
            counter[prefix] += 1
    result = 0
    for prefix, count in counter.items():
        result += count // k
    return result
