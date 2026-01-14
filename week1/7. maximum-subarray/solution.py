from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = best = nums[0]

        for x in nums[1:]:
            cur = max(x, cur + x) # cur 업데이트 _ 지금 보고 있는 위치에서 끝나는 최대 부분합
            best = max(best, cur) # best 업데이트 _ 지금까지 본 모든 부분합 중 최대값
 
        return best
