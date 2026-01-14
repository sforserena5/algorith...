# height가 감소했다가 증가 할 경우 면적이 생김 -> 왼/오른쪽 나눠서 효율적으로 처리
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1 # 왼/오른쪽 나눠서 처리
        left_max = right_max = 0
        water = 0

        while left < right:
            if height[left] <= height[right]:
                # 왼쪽 처리
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                # 오른쪽 처리
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water