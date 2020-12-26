from typing import List


class Solution:
    # 暴力解法
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]

        return []
    # hash
    def twoSumHash(self,nums: List[int],target: int) -> List[int]:
        hashtble = dict()
        for i,num in enumerate(nums):
            if target - num in hashtble:
                return [hashtble[target - num],i]
            hashtble[nums[i]] = i
        return []

s = Solution()
nums = [2,5,3,1,6]
ret = s.twoSumHash(nums,8)
print(ret)