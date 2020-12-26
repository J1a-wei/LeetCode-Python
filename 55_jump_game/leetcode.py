from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n,rightMost = len(nums),0
        for i in range(nums):
            if i <=rightMost:
                rightMost = max(rightMost,i+nums[i])
                if rightMost >= n - 1:
                    return True
        return False
