from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left,right = 0 , len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]

    def findMin2(self,nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left,right = 0 , len(nums) - 1
        if nums[left] < nums[right]:
            return nums[left]

        while left <= right:
            mid = (left + right) >> 1
            if nums[mid + 1] < nums[mid]:
                return nums[mid+1]

            if mid -1 >=0 and nums[mid - 1] > nums[mid]:
                return nums[mid]

            if nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return -1
