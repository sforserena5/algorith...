# Search-In-Rotated-Sorted-Array

- **Link:** [https://leetcode.com/problems/search-in-rotated-sorted-array/]

## 🕒 Trials

- **Trial 1:** Accepted

    class Solution:
        def search(self, nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid

                # 왼쪽 구간이 정렬된 경우
                if nums[left] <= nums[mid]:
                    if nums[left] <= target < nums[mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                        
                # 오른쪽 구간이 정렬된 경우
                else:
                    if nums[mid] < target <= nums[right]:
                        left = mid + 1
                    else:
                        right = mid - 1

            return -1


## 💡 Approach
    중간 값을 기준으로, 항상 한쪽 구간은 정렬되어 있다는 점을 이용하여,
    정렬된 구간에 target이 포함되는지 확인하면서 탐색 범위를 절반씩 줄여 나갔다.

## ⏱️ Time Complexity
    O(n)

## ✍️ Review
- Why did I choose this approach?
회전된 배열의 특성을 이용하면 불필요한 탐색을 줄일 수 있어 target 위치를 효율적으로 찾을 수 있음