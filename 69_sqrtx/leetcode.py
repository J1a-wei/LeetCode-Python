class Solution:
    def mySqrt(self,x: int) -> int:
        if x == 0:
            return 0

        left = 1
        right = x // 2

        while left < right:
            mid = (left + right + 1) >> 1
            square = mid * mid

            if square > x:
                right = mid - 1
            else:
                left = mid

        return left


    def mySqrtError(self,x: int) -> int:
        if x == 0:
            return 0
        left = 1
        right = x // 2

        while left < right:
            import time
            time.sleep(1)
            print('调试代码，观察区间左右端点、中位数，和进入的分支： left = {} , right = {} , '.format(left, right), end='')

            mid = (left + right + 1) >> 1
            print('mid = {},'.format(mid),end='  ')
            sqare = mid * mid

            if sqare < x:
                print('进入 right = mid - 1 这个分支')
                left = mid + 1
            else :
                print('进入 left = mid 这个分支')
                right = mid

        return left





if __name__ == '__main__':
    x = 9
    solution = Solution()
    res = solution.mySqrtError(x)
    print(res)