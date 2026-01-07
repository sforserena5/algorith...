from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)

        for a in range (length):
            for b in range (a + 1, length):
                if nums[a] + nums[b] == target:
                    return [a, b]
        