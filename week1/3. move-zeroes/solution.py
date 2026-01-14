from typing import List
class Solution:
        def moveZeroes(self, nums: List[int]) -> None:
            idx = 0  # non-zero 

            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[idx] = nums[i]
                    idx += 1

            # 남은 자리를 0으로 채우기
            for i in range(idx, len(nums)):
                nums[i] = 0
