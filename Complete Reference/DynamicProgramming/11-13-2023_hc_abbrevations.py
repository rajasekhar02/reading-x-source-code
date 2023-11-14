# First implemented greedy algorithm but fails :
    """First implemented greedy algorithm but fails
        Testcase that fail greed algorithm:
        2
        aABBB // a
        ABBB  // b 
              // ans: True (actual) False (greedy) True(recursion)
    """
def abbreviation(a, b):
    def recurse(i, j):
        if j >= len(b):
            while i < len(a):
                if ord('A') <= ord(a[i]) <= ord('Z'):
                    return False
                i += 1
            return True
        if i >= len(a):
            return False
        ans = False
        if str.lower(a[i]) == str.lower(b[j]):
            ans = recurse(i+1, j+1)
        if ord('a') <= ord(a[i]) <= ord('z'):
            ans = ans or recurse(i+1, j)
        return ans
    return 'YES' if recurse(0, 0) else 'NO'