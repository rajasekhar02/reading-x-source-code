class Solution:
    def checkValidStringTwoStacks(self, s: str) -> bool:
        stackForOpenBraces = deque()
        stackForStars = deque()
        for id,i in enumerate(s):
            if i == "(":
                stackForOpenBraces.append(id)
            if i == "*":
                stackForStars.append(id)
            elif i == ")":
                if len(stackForOpenBraces) > 0:
                    stackForOpenBraces.pop()
                elif len(stackForStars) > 0:
                    stackForStars.pop()
                else:
                    return False
        while stackForOpenBraces and stackForStars:
            if stackForOpenBraces.pop() > stackForStars.pop():
                return False
        return not stackForOpenBraces
    
