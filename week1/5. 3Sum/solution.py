from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [] 

        for i in range(len(nums)):
            # i 중복 제거
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # nums[i]가 0보다 크면 뒤도 전부 0보다 크거나 같으므로 합이 0 불가
            if nums[i] > 0:
                break

            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # left 중복 제거
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    # right 중복 제거
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return res
