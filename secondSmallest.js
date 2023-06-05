// second largest element in the array
let elements = [1, 3, 2, 5, 4]//[3, 2, 1, 2, 3]//[5, 5, 5, 5, 5]//[4, 3, 2, 1, 1]// [1,16,3,24,2,15];

let maxRecurrence = function (list, pos, comparedElements) {
    if (pos >= (list.length - 1)) {
        return list[pos]
    }
    let maxEleFromChild = maxRecurrence(list, pos + 1, comparedElements)
    if (comparedElements[list[pos]] == undefined) {
        comparedElements[list[pos]] = []
    }
    if (comparedElements[maxEleFromChild] == undefined) {
        comparedElements[maxEleFromChild] = []
    }
    comparedElements[list[pos]].push(maxEleFromChild)
    comparedElements[maxEleFromChild].push(list[pos])
    return Math.max(list[pos], maxEleFromChild)
}

let maxRecurrence2 = function (list, comparedElements) {
    let newList = []
    if (list.length == 1) {
        return list[0]
    }
    for (let i = 0; i < list.length - 1; i += 2) {
        console.log(list[i], list[i + 1])
        if (comparedElements[list[i]] === undefined) {
            comparedElements[list[i]] = []
        }
        if (comparedElements[list[i + 1]] === undefined) {
            comparedElements[list[i + 1]] = []
        }
        comparedElements[list[i]].push(list[i + 1])
        comparedElements[list[i + 1]].push(list[i])
        newList.push(Math.max(list[i], list[i + 1]))
    }
    if ((list.length & 1)) {
        newList.push(list[list.length - 1])
    }
    return maxRecurrence2(newList, comparedElements);
}

comparedElements = {}
maxE = maxRecurrence2(elements, comparedElements)
console.log(maxE, comparedElements)
newComparedElements = {}
maxRecurrence2(comparedElements[maxE], newComparedElements)
