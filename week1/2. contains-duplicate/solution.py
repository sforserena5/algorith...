from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set()
        for a in nums:
            if a in duplicate:
                return True
            duplicate.add(a)
        return False
    
 