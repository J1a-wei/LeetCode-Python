from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 :
            return -1
        if len(nums)==1 and nums[0] == target:
            return 0

        if len(nums)==1 and nums[0] != target:
            return -1

        left ,right = 0,len(nums) - 1
        while left <= right:
            mid = int(left + (right - left ) / 2)
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if target >= nums[left] and target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target>=nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

if __name__ == "__main__":
    l = [3,1]
    solution = Solution()
    res = solution.search(l,1)
    print(res)