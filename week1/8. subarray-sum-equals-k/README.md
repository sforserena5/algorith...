# Subaarry-sum-equals-k

- **Link:** [https://leetcode.com/problems/subarray-sum-equals-k/]

## 🕒 Trials

- **Trial 1:** Accepted

    class Solution:
        def subarraySum(self, nums: List[int], k: int) -> int:
            count = 0

            for i in range(len(nums)):
                sum = 0
                for j in range(i, len(nums)):
                    sum += nums[j]
                    if sum == k:
                        count +=1
            return count



## 💡 Approach
    리스트 각 원소를 시작점으로 잡고, 다음의 원소들을 하나씩 더해가며 부분 배열의 합을 계산함
    합이 k와 같아지는 경우마다 카운트를 증가시켜 조건을 만족하는 모든 연속 부분 배열의 개수를 구했다

## ⏱️ Time Complexity
    O(n^2)

## ✍️ Review
- Why did I choose this approach?
    연속된 부분 배열을 직접 탐색하면서 합을 계산하기 때문에 로직이 명확함!