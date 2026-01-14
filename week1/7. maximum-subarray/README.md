# Maximum Subarray

- **Link:** [https://leetcode.com/problems/maximum-subarray/description/]

## 🕒 Trials

- **Trial 1:** Accepted

    class Solution:
        def maxSubArray(self, nums: List[int]) -> int:
            cur = best = nums[0]

            for x in nums[1:]:
                cur = max(x, cur + x) # cur 업데이트 _ 지금 보고 있는 위치에서 끝나는 최대 부분합
                best = max(best, cur) # best 업데이트 _ 지금까지 본 모든 부분합 중 최대값
    
            return best


## 💡 Approach
    연속된 부분 배열의 합을 구하는 문제이므로,
    배열을 왼쪽부터 하나씩 순회하면서 현재 위치까지의 최대 부분합을 유지하는 방식으로 접근했다.
    테스트 3개 통과함!

## ⏱️ Time Complexity

    O(n)
    배열을 한 번만 순회하므로

## ✍️ Review

- Why did I choose this approach?
    이 문제의 입력 크기가 크기 때문에 모든 부분 배열을 검사하는 방식은 비효율적이라고 판단했다.
    현재까지의 합이 음수가 되는 순간 이후의 합에 오히려 손해가 된다는 점에 착안하여,
    부분 배열을 계속 유지할지 아니면 새로 시작할지를 매 단계에서 결정하는 방식이 가장 효율적이라고 생각했다. 