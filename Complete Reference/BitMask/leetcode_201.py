class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
      if left == 0:
        return 0
      ans = left & right
      diff = right - left
      if diff == 0:
        return ans
      for i in range(0, 32):
        pow2 = 1<<i
        if not (ans & pow2):
            continue
        if diff >= (pow2):
            ans = ans & ~(pow2)
      return ans
  def solution2(self, left:int, right:int)->int:
    # common prefix identification
    cnt = 0
    while left != right:
      left >>= 1
      right >>= 1
      cnt+=1
    return (left << cnt)
  def solution3(self, left:int, right:int) -> int:
    if left == 0:
      return 0
    while right > left:
      right &= (right - 1)
    return right
