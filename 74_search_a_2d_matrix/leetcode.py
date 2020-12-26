from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        left, right = 0 , m * n - 1
        while left <= right:
            mid_id = (left + right) // 2
            mid = matrix[mid_id // n][mid_id % n]
            if target == mid:
                return True
            else:
                if target < mid:
                    right = mid_id - 1
                else:
                    left = mid_id + 1
        return False

if __name__ =='__main__':
    matrix = [[1,3,5,7],
              [10,11,16,20],
              [23,30,34,60]
              ]
    target = 3
    solution = Solution()
    res = solution.searchMatrix(matrix,target)
    print(res)
    print(3 + 1 >> 1)