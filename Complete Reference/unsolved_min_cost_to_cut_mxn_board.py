def minimumCost(rowCostArr, colCostArr, l, w):
    rowCostArr = sorted(rowCostArr, reverse=True)
    colCostArr = sorted(colCostArr, reverse=True)
    cost = 0
    iRowCost = 0
    jColCost = 0
    boardCntByRow = 1
    boardCntByCol = 1
    while iRowCost < l - 1 and jColCost < w - 1:
        if rowCostArr[iRowCost] > colCostArr[jColCost]:
            cost += rowCostArr[iRowCost] * boardCntByCol
            iRowCost += 1
            boardCntByRow += 1
        else:
            cost += colCostArr[jColCost] * boardCntByRow
            jColCost += 1
            boardCntByCol += 1
    rowSum = 0
    while iRowCost < l - 1:
        rowSum += rowCostArr[iRowCost]
        iRowCost += 1

    cost += rowSum * boardCntByCol

    colSum = 0
    while jColCost < w - 1:
        colSum += colCostArr[jColCost]
        jColCost += 1

    cost += colSum * boardCntByRow

    return cost


def minimumCostBF(row, column, l, w):
    # Write your code here
    # Return an integer
    return recurse(l, w, row, column)


def recurse(row, column, l, w):
    if row == 1:
        return sum(w)
    if column == 1:
        return sum(l)
    maxLen = 0
    maxLIndex = 0
    for i in range(0, len(l)):
        if maxLen < l[i]:
            maxLen = l[i]
            maxLIndex = i
    maxWid = 0
    maxWIndex = 0
    for i in range(0, len(w)):
        if maxWid < w[i]:
            maxWid = w[i]
            maxWIndex = i
    if maxLen > maxWid:
        return (
            maxLen
            + recurse(maxLIndex + 1, column, l[:maxLIndex], w)
            + recurse(row - maxLIndex - 1, column, l[maxLIndex + 1 :], w)
        )
    return (
        maxWid
        + recurse(row, maxWIndex + 1, l, w[:maxWIndex])
        + recurse(row, column - maxWIndex - 1, l, w[maxWIndex + 1 :])
    )
