from typing import List, Tuple


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = self.recurse(s, 0, 0)
        return ans

    def recurse(self, s: str, start: int, end: int) -> List[List[str]]:
        size = len(s)
        if end == (size - 1):
            if self.is_palindrome(s[start : end + 1]):
                return [[s[start : end + 1]]]
            return []
        ans = self.recurse(s, start, end + 1)
        curr_substr = s[start : end + 1]
        if self.is_palindrome(curr_substr):
            substrings = self.recurse(s, end + 1, end + 1)
            for i in substrings:
                ans.append([*i, curr_substr])
        return ans

    def is_palindrome(self, s):
        size = len(s)
        for i in range(0, len(s) >> 1):
            if s[i] != s[size - i - 1]:
                return False
        return True


s = "aaa"
print(Solution().partition(s))
