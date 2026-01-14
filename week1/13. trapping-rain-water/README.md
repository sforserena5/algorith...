# Trapping Rain Water

- **Link:** [https://leetcode.com/problems/trapping-rain-water/]

## 🕒 Trials

- **Trial 1:** Accepted..but gpt 도움 받음!!

    class Solution:
        def trap(self, height: List[int]) -> int:
            left, right = 0, len(height) - 1 # 왼/오른쪽 나눠서 처리
            left_max = right_max = 0
            water = 0

            while left < right:
                if height[left] <= height[right]:
                    # 왼쪽
                    if height[left] >= left_max:
                        left_max = height[left]
                    else:
                        water += left_max - height[left]
                    left += 1
                else:
                    # 오른쪽
                    if height[right] >= right_max:
                        right_max = height[right]
                    else:
                        water += right_max - height[right]
                    right -= 1

            return water

## 💡 Approach  
    왼쪽과 오른쪽에서 각각의 최대 높이를 유지하면서, 현재 위치에서 고일 수 있는 물의 양을 계산해 누적했다. 포인터를 각각 안쪽으로 이동시키며 모든 칸을 1번씩 확인함
## ⏱️ Time Complexity
    O(n)

## ✍️ Review
- Why did I choose this approach?
    각 칸에 고이는 물의 양은 양쪽에서의 최대 높이에 의해 결정되므로 효율적으로 계산하기 위해 투포인터 방식을 선택했다.