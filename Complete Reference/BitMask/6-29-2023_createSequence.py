def createSequence(n):
    # Write your code here.
    nums = {
        "0" : "2",
        "1" : "5"
    }
    i = 1
    ans = []
    while True:
        i += 1
        strI = format(i, "b")
        j = 1
        curr = int(
            "".join(
                list(
                    map(lambda x: nums[strI[x]], range(1, len(strI)))
                )
            )
        )
        if curr > n:
            break
        ans.append(curr)
    return ans