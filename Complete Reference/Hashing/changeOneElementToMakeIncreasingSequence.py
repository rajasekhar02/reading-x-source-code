
def solution(numbers):
    newList = numbers[:]
    usedSwap = 0
    for i in range(1,len(newList)-1):
        if numbers[i] > numbers[i-1] and numbers[i] < numbers[i+1]:
            continue
        if numbers[i-1] >= numbers[i] < numbers[i+1] and not usedSwap:  
            lowEle = -1
            if i > 1:
                lowEle = numbers[i-2]
            val = foundSwap(getSwaps(numbers[i-1]), lowEle , numbers[i])
            if val > -1:
                numbers[i-1] = val
                usedSwap = 1
            else: 
                return False
        elif numbers[i-1] < numbers[i] >= numbers[i+1] and numbers[i-1] < numbers[i+1] and not usedSwap: 
            val = foundSwap(getSwaps(numbers[i]), numbers[i-1] , numbers[i+1])
            if val > -1:
                numbers[i] = val
                usedSwap = 1
            else:
                return False
        elif numbers[i-1] < numbers[i] >= numbers[i+1] and numbers[i-1] > numbers[i+1] and not usedSwap: 
            high = 1001
            if i < len(newList)-2:
                high = numbers[i+2]
            val = foundSwap(getSwaps(numbers[i+1]), numbers[i] , high)
            if val > -1:
                numbers[i+1] = val
                usedSwap = 1
            else:
                return False
        else:
            return False
    return True

def foundSwap(swaps,lowNum, highNum):
    foundSwap = -1
    for prev in swaps:
        if lowNum < prev < highNum:
            foundSwap = prev
            break
    return foundSwap

def getSwaps(number):
    swaps = []
    numStr = list(str(number))
    length = len(numStr)
    for k in range(0,length):
        for l in range(k+1, length):
            tempStr = numStr[:]
            tempC = tempStr[l]
            tempStr[l] = tempStr[k]
            tempStr[k] = tempC
            swaps.append(int("".join(tempStr)))
    return swaps