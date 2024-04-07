class Solution:
    def checkValidString(self, s:str) -> bool:
        len_str = len(s)  
        dp = [[False]*(len_str+1) for i in range(len_str + 1)]
        dp[len_str][0] = True 
        for pos in range(len_str-1, -1, -1):
            for open_braces in range(len_str):
                is_valid = False
                if s[pos] == "*":
                    if open_braces < len_str:
                        is_valid |= dp[pos+1][open_braces+1]
                    if open_braces > 0:
                        is_valid |= dp[pos+1][open_braces-1]
                    is_valid |= dp[pos+1][open_braces]
                else:
                    if s[pos] == "(":
                        is_valid |= dp[pos + 1][open_braces + 1]
                    elif open_braces > 0:
                        is_valid |= dp[pos + 1][open_braces - 1]
                dp[pos][open_braces] = is_valid
        return dp[0][0]
    def checkValidStringTD(self, s: str) -> bool:
        len_str = len(s)  
        dp = [[-1]*len_str for i in range(len_str + 1)]          
        def recursion(pos, countOpenBraces):
            if pos == len_str:
                return countOpenBraces == 0
            if dp[pos][countOpenBraces] != -1:
                return dp[pos][countOpenBraces] == 1
            is_valid = False
            if s[pos] == "(":
                is_valid = recursion(pos+1, countOpenBraces+1)
            if s[pos] == ")" and countOpenBraces > 0:
                is_valid = recursion(pos+1, countOpenBraces-1)
            elif s[pos] == "*":
                is_valid |= recursion(pos+1, countOpenBraces+1)
                if countOpenBraces > 0:
                    is_valid |= recursion(pos+1, countOpenBraces-1)
                is_valid |= recursion(pos+1, countOpenBraces)
            dp[pos][countOpenBraces] = 1 if is_valid else 0
            return is_valid
        return recursion(0, 0)
    
