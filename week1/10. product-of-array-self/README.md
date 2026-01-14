# Search-In-Rotated-Sorted-Array

- **Link:** [https://leetcode.com/problems/search-in-rotated-sorted-array/]

## 🕒 Trials

- **Trial 1:** Accepted

    class Solution:
        def productExceptSelf(self, nums: List[int]) -> List[int]:
            answer = [1] * len(nums)   # output될 리스트

            # 왼쪽 곱
            left = 1
            for i in range(len(nums)):
                answer[i] = left
                left *= nums[i]

            # 오른쪽 곱
            right = 1
            for i in range(len(nums)- 1, -1, -1):
                answer[i] *= right
                right *= nums[i]

            return answer

## 💡 Approach
    왼쪽에 있는 값들의 곱과 오른쪽에 있는 값들의 곱을 나누어 계산했다.
    먼저 왼쪽부터 누적 곱을 저장한 뒤, 오른쪽에서부터 다시 순회하며 해당 값을 곱했다.

## ⏱️ Time Complexity
    O(n)

## ✍️ Review
- Why did I choose this approach?
    배열을 한 번씩만 순회하면서 계산할 수 있는 누적 곱 방식을 택함      