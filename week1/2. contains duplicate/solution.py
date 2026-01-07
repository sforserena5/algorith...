from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        i = len(nums) #4
        for a in range(0,i): #(0, 4, 1) 0, 1, 2, 3
            for b in range (a+1, i):
                if nums[a] == nums [b]:
                    return True
            return False