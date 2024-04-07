class Solution:
    def checkValidString2Pointers(self, s:str)->bool:
        len_str = len(s) - 1
        countOpenBraces = 0
        countClosedBraces = 0
        for i in range(0, len_str+1):
            if s[i] == "(" or s[i] == "*":
                countOpenBraces += 1
            else:
                countOpenBraces -= 1
            if s[len_str - i] == ")" or s[len_str - i] == "*":
                countClosedBraces += 1
            else:
                countClosedBraces -= 1
            if countOpenBraces < 0 or countClosedBraces < 0:
                return False
        return True
