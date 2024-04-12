from typing import List
class Solution:
    def trap3(self, height: List[int]) -> int:
        stack  = []
        ans = 0
        removable_area = 0
        for r_idx, r_h in enumerate(height):
            while stack and height[stack[-1]] < r_h:
                m_idx = stack.pop()
                if not stack: break
                l_idx = stack[-1]
                res_h = min(r_h, height[l_idx]) - height[m_idx]
                res_w = r_idx - l_idx - 1
                ans += res_w * res_h
            stack.append(r_idx)
        return ans
    def trap(self, height:List[int]) ->int:
        # if i coded solution for [1,0,3,0,6,0,3,0,1] then it will work for every solution
        maxLeft = 0
        left = 0
        maxRight = 0 
        right = len(height) - 1
        ans = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > maxLeft:
                    maxLeft = height[left]
                else:
                    ans += maxLeft - height[left]
                left += 1
            else:
                if height[right] > maxRight:
                    maxRight = height[right]
                else:
                    ans += maxRight - height[right]
                right -= 1
        return ans
    def trap2(self, height: List[int]) -> int:
        low = 0
        low_itr = 1
        right = len(height) - 1
        right_itr = right - 1
        removable_area_left = 0
        removable_area_right = 0
        ans_area = 0
        while low != right:
            # print(low, low_itr, right, right_itr, ans_area, removable_area_left, removable_area_right)
            if height[low] <= height[right]:
                if low_itr < (len(height)-1) and height[low_itr] < height[low]:
                    removable_area_left += height[low_itr]
                    low_itr += 1
                else:
                    ans_area += ((low_itr - low - 1) * height[low]) - removable_area_left
                    low = low_itr
                    low_itr = low_itr + 1
                    removable_area_left = 0
            else:
                if right_itr > 0 and  height[right_itr] < height[right]:
                    removable_area_right += height[right_itr]
                    right_itr -= 1
                else:
                    ans_area += ((right - right_itr - 1) * height[right]) - removable_area_right
                    right = right_itr
                    right_itr = right - 1
                    removable_area_right = 0
        return ans_area
